# Databricks notebook source
# MAGIC %md
# MAGIC # Healthcare Data Engineering Pipeline
# MAGIC **Architecture:** Source -> Bronze -> Silver -> Gold
# MAGIC
# MAGIC This notebook implements the Celebal internship healthcare pipeline using
# MAGIC Python, PySpark, Spark SQL and Delta Lake.
# MAGIC
# MAGIC **Important:** The supplied source does not contain a true patient identifier.
# MAGIC A deterministic composite business key (normalized Name + Gender + Blood Type)
# MAGIC is generated for SCD Type 2 demonstration. In production, replace it with the
# MAGIC source-system patient ID.

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

SOURCE_PATH = "/Volumes/<catalog>/<schema>/<volume>/patients_records.csv"
BRONZE_TABLE = "bronze_patients"
SILVER_TABLE = "silver_patients"
SCD_TABLE = "dim_patient_scd2"

# COMMAND ----------
# MAGIC %md
# MAGIC ## 1. Ingest source data

# COMMAND ----------

raw_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(SOURCE_PATH)
)

display(raw_df)

# COMMAND ----------
# MAGIC %md
# MAGIC ## 2. Data quality checks

# COMMAND ----------

print("Rows:", raw_df.count())
print("Columns:", len(raw_df.columns))

null_check = raw_df.select([
    F.sum(F.col(c).isNull().cast("int")).alias(c)
    for c in raw_df.columns
])
display(null_check)

print("Duplicate rows:", raw_df.count() - raw_df.distinct().count())

# COMMAND ----------
# MAGIC %md
# MAGIC ## 3. Bronze layer
# MAGIC Bronze preserves the source data without business transformations.

# COMMAND ----------

(
    raw_df.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(BRONZE_TABLE)
)

# COMMAND ----------
# MAGIC %md
# MAGIC ## 4. Silver transformation

# COMMAND ----------

bronze_df = spark.table(BRONZE_TABLE)

silver_df = (
    bronze_df
    .select(
        F.col("Name").cast("string").alias("patient_name"),
        F.col("Age").cast("int").alias("age"),
        F.col("Gender").cast("string").alias("gender"),
        F.col("Blood Type").cast("string").alias("blood_type"),
        F.col("Medical Condition").cast("string").alias("medical_condition"),
        F.to_date("Date of Admission", "yyyy-MM-dd").alias("admission_date"),
        F.col("Doctor").cast("string").alias("doctor"),
        F.col("Hospital").cast("string").alias("hospital"),
        F.col("Insurance Provider").cast("string").alias("insurance_provider"),
        F.col("Billing Amount").cast("double").alias("billing_amount"),
        F.col("Room Number").cast("int").alias("room_number"),
        F.col("Admission Type").cast("string").alias("admission_type"),
        F.to_date("Discharge Date", "yyyy-MM-dd").alias("discharge_date"),
        F.col("Medication").cast("string").alias("medication"),
        F.col("Test Results").cast("string").alias("test_results")
    )
    .withColumn("patient_name", F.trim("patient_name"))
    .withColumn("gender", F.trim("gender"))
    .withColumn("blood_type", F.upper(F.trim("blood_type")))
    .withColumn("medical_condition", F.trim("medical_condition"))
    .withColumn("hospital", F.trim("hospital"))
    .withColumn("insurance_provider", F.trim("insurance_provider"))
    .withColumn("admission_type", F.trim("admission_type"))
    .withColumn("medication", F.trim("medication"))
    .withColumn("test_results", F.trim("test_results"))
    .dropDuplicates()
    .withColumn(
        "length_of_stay_days",
        F.datediff(F.col("discharge_date"), F.col("admission_date"))
    )
    .withColumn(
        "patient_business_key",
        F.sha2(
            F.concat_ws(
                "|",
                F.lower(F.trim(F.col("patient_name"))),
                F.lower(F.trim(F.col("gender"))),
                F.upper(F.trim(F.col("blood_type")))
            ),
            256
        )
    )
    .withColumn(
        "record_id",
        F.sha2(
            F.concat_ws(
                "|",
                F.col("patient_business_key"),
                F.coalesce(F.date_format("admission_date", "yyyy-MM-dd"), F.lit("")),
                F.lower(F.trim(F.col("hospital")))
            ),
            256
        )
    )
)

# Basic data-quality filter
silver_df = silver_df.filter(
    F.col("patient_name").isNotNull() &
    F.col("admission_date").isNotNull() &
    F.col("hospital").isNotNull()
)

# COMMAND ----------
# MAGIC %md
# MAGIC ## 5. Save Silver layer

# COMMAND ----------

(
    silver_df.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(SILVER_TABLE)
)

display(silver_df.limit(20))

# COMMAND ----------
# MAGIC %md
# MAGIC ## 6. SCD Type 2 dimension
# MAGIC
# MAGIC The source file does not provide a stable patient ID. The generated business key
# MAGIC is therefore used for demonstration. `MERGE` closes the old version and inserts
# MAGIC the new version when tracked attributes change.

# COMMAND ----------

from delta.tables import DeltaTable

scd_source = (
    silver_df
    .select(
        "patient_business_key", "patient_name", "age", "gender", "blood_type",
        "medical_condition", "insurance_provider", "hospital"
    )
    .dropDuplicates(["patient_business_key"])
    .withColumn("effective_start_date", F.current_date())
    .withColumn("effective_end_date", F.lit(None).cast("date"))
    .withColumn("is_current", F.lit(True))
)

if not spark.catalog.tableExists(SCD_TABLE):
    (
        scd_source.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(SCD_TABLE)
    )
else:
    target = DeltaTable.forName(spark, SCD_TABLE)

    changed = (
        "target.patient_name <> source.patient_name OR "
        "target.age <> source.age OR "
        "target.gender <> source.gender OR "
        "target.blood_type <> source.blood_type OR "
        "target.medical_condition <> source.medical_condition OR "
        "target.insurance_provider <> source.insurance_provider OR "
        "target.hospital <> source.hospital"
    )

    (
        target.alias("target")
        .merge(
            scd_source.alias("source"),
            "target.patient_business_key = source.patient_business_key "
            "AND target.is_current = true"
        )
        .whenMatchedUpdate(
            condition=changed,
            set={
                "effective_end_date": "current_date()",
                "is_current": "false"
            }
        )
        .execute()
    )

    # Insert current versions that are new or were changed
    current_keys = (
        spark.table(SCD_TABLE)
        .filter("is_current = true")
        .select("patient_business_key")
    )

    new_versions = (
        scd_source.alias("s")
        .join(current_keys.alias("t"), "patient_business_key", "left_anti")
    )

    (
        new_versions.write
        .format("delta")
        .mode("append")
        .saveAsTable(SCD_TABLE)
    )

display(spark.table(SCD_TABLE).limit(20))

# COMMAND ----------
# MAGIC %md
# MAGIC ## 7. Gold layer - hospital statistics

# COMMAND ----------

gold_hospital = (
    silver_df.groupBy("hospital")
    .agg(
        F.count("*").alias("patient_count"),
        F.sum("billing_amount").alias("total_billing"),
        F.avg("billing_amount").alias("average_billing"),
        F.avg("age").alias("average_age"),
        F.avg("length_of_stay_days").alias("average_length_of_stay_days")
    )
    .withColumn(
        "hospital_rank",
        F.dense_rank().over(
            Window.orderBy(F.desc("patient_count"))
        )
    )
)

gold_hospital.write.format("delta").mode("overwrite").option(
    "overwriteSchema", "true"
).saveAsTable("gold_hospital_statistics")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 8. Gold layer - condition statistics

# COMMAND ----------

gold_condition = (
    silver_df.groupBy("medical_condition")
    .agg(
        F.count("*").alias("patient_count"),
        F.sum("billing_amount").alias("total_billing"),
        F.avg("billing_amount").alias("average_billing")
    )
    .orderBy(F.desc("patient_count"))
)

gold_condition.write.format("delta").mode("overwrite").option(
    "overwriteSchema", "true"
).saveAsTable("gold_condition_statistics")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 9. Gold layer - admission statistics

# COMMAND ----------

gold_admission = (
    silver_df.groupBy("admission_type")
    .agg(
        F.count("*").alias("patient_count"),
        F.avg("billing_amount").alias("average_billing")
    )
    .orderBy(F.desc("patient_count"))
)

gold_admission.write.format("delta").mode("overwrite").option(
    "overwriteSchema", "true"
).saveAsTable("gold_admission_statistics")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 10. Gold layer - insurance statistics

# COMMAND ----------

gold_insurance = (
    silver_df.groupBy("insurance_provider")
    .agg(
        F.count("*").alias("patient_count"),
        F.sum("billing_amount").alias("total_billing"),
        F.avg("billing_amount").alias("average_billing")
    )
    .orderBy(F.desc("patient_count"))
)

gold_insurance.write.format("delta").mode("overwrite").option(
    "overwriteSchema", "true"
).saveAsTable("gold_insurance_statistics")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 11. Gold layer - overall patient statistics

# COMMAND ----------

gold_patient = silver_df.agg(
    F.count("*").alias("total_patient_records"),
    F.countDistinct("patient_business_key").alias("unique_patient_business_keys"),
    F.countDistinct("hospital").alias("total_hospitals"),
    F.countDistinct("doctor").alias("total_doctors"),
    F.avg("age").alias("average_age"),
    F.sum("billing_amount").alias("total_billing"),
    F.avg("billing_amount").alias("average_billing"),
    F.avg("length_of_stay_days").alias("average_length_of_stay_days")
)

gold_patient.write.format("delta").mode("overwrite").option(
    "overwriteSchema", "true"
).saveAsTable("gold_patient_statistics")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 12. Verify Gold layer

# COMMAND ----------

display(spark.table("gold_hospital_statistics").orderBy("hospital_rank").limit(20))
display(spark.table("gold_condition_statistics"))
display(spark.table("gold_admission_statistics"))
display(spark.table("gold_insurance_statistics"))
display(spark.table("gold_patient_statistics"))

# COMMAND ----------
# MAGIC %md
# MAGIC ## 13. Spark SQL examples

# COMMAND ----------

spark.sql("""
SELECT hospital, patient_count, average_billing, hospital_rank
FROM gold_hospital_statistics
ORDER BY hospital_rank, hospital
LIMIT 20
""").show()

spark.sql("""
SELECT medical_condition, patient_count, total_billing
FROM gold_condition_statistics
ORDER BY patient_count DESC
""").show()
