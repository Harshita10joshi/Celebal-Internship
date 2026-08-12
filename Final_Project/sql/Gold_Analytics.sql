-- Healthcare Gold Layer Analytics
-- Run after the Databricks PySpark notebook has created the tables.

SELECT * FROM gold_patient_statistics;

SELECT hospital, patient_count, total_billing, average_billing, hospital_rank
FROM gold_hospital_statistics
ORDER BY hospital_rank, hospital
LIMIT 20;

SELECT medical_condition, patient_count, total_billing, average_billing
FROM gold_condition_statistics
ORDER BY patient_count DESC;

SELECT admission_type, patient_count, average_billing
FROM gold_admission_statistics
ORDER BY patient_count DESC;

SELECT insurance_provider, patient_count, total_billing, average_billing
FROM gold_insurance_statistics
ORDER BY patient_count DESC;

-- Example KPI queries
SELECT SUM(patient_count) AS total_records
FROM gold_hospital_statistics;

SELECT hospital, patient_count
FROM gold_hospital_statistics
ORDER BY patient_count DESC
LIMIT 10;
