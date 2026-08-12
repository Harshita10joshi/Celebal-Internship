# Healthcare Data Pipeline — Celebal Internship Final Project

## Project overview
This project implements a scalable healthcare data engineering pipeline using a Medallion Architecture:
**Source → Bronze → Silver → Gold → Analytics**.

The supplied healthcare dataset contains **55,500 source rows and 15 columns**. Local validation found **534 duplicate rows** and **0 null cells**.

## Technology stack
- Python
- PySpark
- Spark SQL
- Databricks
- Delta Lake
- AWS S3 / ADLS / Databricks Volumes as source options
- Lakeflow Declarative Pipelines / DLT as an automation option
- Power BI / Databricks SQL for analytics
- Kafka as future real-time extension

## Architecture

```text
patients_records.csv
        |
        v
   Source Storage
        |
        v
   Bronze Delta Table
        |
        | cleaning / standardization / deduplication
        v
   Silver Delta Table
        |
        | aggregations
        v
   Gold Delta Tables
        |
        +------> Power BI / Databricks SQL
        |
        +------> Future MLOps / Predictive Analytics
```

## Repository structure

```text
Healthcare_Data_Pipeline/
├── data/
│   └── patients_records.csv
├── notebooks/
│   ├── Healthcare_Data_Pipeline.py
│   └── Healthcare_Data_Pipeline.ipynb
├── sql/
│   └── Gold_Analytics.sql
├── pipeline/
│   └── Lakeflow_DLT_SQL.sql
├── docs/
│   └── PowerBI_Dashboard_Specification.md
├── sample_gold_outputs/
│   ├── gold_patient_statistics.csv
│   ├── gold_hospital_statistics.csv
│   ├── gold_condition_statistics.csv
│   ├── gold_admission_statistics.csv
│   └── gold_insurance_statistics.csv
└── README.md
```

## Bronze layer
The raw source is stored as a Delta table named `bronze_patients`. The Bronze layer is intentionally preserved without business transformations to maintain traceability and reproducibility.

## Silver layer
The Silver layer is stored as `silver_patients` and performs:
- column standardization
- date conversion
- data type conversion
- whitespace/format cleanup
- duplicate removal
- basic data-quality filtering
- derived length-of-stay metric
- deterministic business-key generation

## SCD Type 2
The project includes an SCD Type 2 dimension named `dim_patient_scd2`.

The supplied CSV does not contain a true patient ID. Therefore the notebook creates a deterministic composite business key from normalized patient name, gender and blood type **for demonstration purposes**. In a production implementation, this should be replaced by the source-system patient identifier.

SCD Type 2 fields:
- `effective_start_date`
- `effective_end_date`
- `is_current`

Delta `MERGE` logic is used to close an old current record when tracked attributes change and append the new version.

## Gold layer
The notebook creates:
- `gold_patient_statistics`
- `gold_hospital_statistics`
- `gold_condition_statistics`
- `gold_admission_statistics`
- `gold_insurance_statistics`

These tables support hospital rankings, patient counts, billing analysis, condition analysis and insurance analysis.

## How to run in Databricks

1. Create/open a Databricks workspace.
2. Upload `data/patients_records.csv` to a Databricks Volume or cloud storage.
3. Open `notebooks/Healthcare_Data_Pipeline.py` as a Databricks notebook.
4. Replace only `SOURCE_PATH` with the actual uploaded file path.
5. Attach a Databricks compute resource.
6. Run all cells.
7. Verify the Bronze, Silver, SCD2 and Gold Delta tables.
8. Connect Power BI or Databricks SQL to the Gold tables using the dashboard specification.

### One unavoidable environment-specific step
The only part that cannot be preconfigured from outside your Databricks account is the **actual source path, workspace/compute, and credentials/permissions**. Everything else is prepared in this package.

## Important project explanation
The current implementation is batch-based. For real-time ingestion, the source can be extended with Kafka/Event Hubs/Kinesis and the streaming data can feed the Bronze layer.

## Future MLOps use cases
Gold data can support:
- high-risk patient prediction
- hospital workload forecasting
- billing trend prediction
- model monitoring and retraining

## Evaluation talking points
- Bronze preserves raw data.
- Silver improves data quality.
- Gold contains business-ready aggregations.
- Delta Lake provides ACID transactions and reliable table management.
- SCD Type 2 preserves historical versions.
- `MERGE` supports insert/update history handling.
- PySpark provides distributed processing.
- Current processing is batch; Kafka is a future streaming extension.
