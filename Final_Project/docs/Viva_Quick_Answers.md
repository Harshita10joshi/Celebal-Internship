# Viva / Evaluation Quick Answers

**Why Medallion Architecture?**
It separates raw ingestion, data quality/transformation and business-ready analytics, making the pipeline easier to maintain and troubleshoot.

**Why Bronze?**
To preserve source data and provide traceability/reprocessing capability.

**Why Silver?**
To clean, standardize and validate data before analytics.

**Why Gold?**
To provide business-ready aggregated tables for dashboards and reporting.

**What is SCD Type 2?**
A method of retaining historical versions of dimension records instead of overwriting previous values.

**Why MERGE?**
MERGE combines matching and non-matching record handling and is useful for incremental Delta Lake updates.

**Why Delta Lake?**
It provides ACID transactions, schema management and reliable table operations on data lake storage.

**Why PySpark?**
It supports distributed processing and scales better than single-machine processing for large datasets.

**Why not clean in Bronze?**
Bronze should preserve the original source to maintain traceability.

**Does the source contain nulls?**
The supplied dataset has no null cells, but the Silver pipeline still performs explicit null validation.

**How many duplicates were found?**
534 exact duplicate rows in the supplied source.

**Is it real-time?**
No. The current implementation is batch-based. Kafka can be added for real-time ingestion.

**What is the SCD limitation in this dataset?**
The source does not provide a stable patient ID, so the project generates a deterministic composite business key for demonstration. A production system should use a real source-system patient ID.

**What can Power BI show?**
Patient counts, hospital rankings, average/total billing, condition analysis, admission analysis and insurance analysis.
