-- Optional Lakeflow Declarative Pipelines / DLT-style definition.
-- Adjust the source path to your Databricks Volume or cloud storage location.

CREATE OR REFRESH STREAMING TABLE bronze_patients_dlt
AS SELECT * FROM cloud_files(
  '/Volumes/<catalog>/<schema>/<volume>/',
  'csv',
  map('header','true','inferSchema','true')
);

CREATE OR REFRESH MATERIALIZED VIEW silver_patients_dlt
AS
SELECT
  trim(Name) AS patient_name,
  CAST(Age AS INT) AS age,
  trim(Gender) AS gender,
  upper(trim(`Blood Type`)) AS blood_type,
  trim(`Medical Condition`) AS medical_condition,
  to_date(`Date of Admission`) AS admission_date,
  trim(Doctor) AS doctor,
  trim(Hospital) AS hospital,
  trim(`Insurance Provider`) AS insurance_provider,
  CAST(`Billing Amount` AS DOUBLE) AS billing_amount,
  CAST(`Room Number` AS INT) AS room_number,
  trim(`Admission Type`) AS admission_type,
  to_date(`Discharge Date`) AS discharge_date,
  trim(Medication) AS medication,
  trim(`Test Results`) AS test_results
FROM LIVE.bronze_patients_dlt
WHERE Name IS NOT NULL
  AND Hospital IS NOT NULL;

CREATE OR REFRESH MATERIALIZED VIEW gold_hospital_statistics_dlt
AS
SELECT
  hospital,
  COUNT(*) AS patient_count,
  SUM(billing_amount) AS total_billing,
  AVG(billing_amount) AS average_billing,
  AVG(age) AS average_age,
  AVG(DATEDIFF(discharge_date, admission_date)) AS average_length_of_stay_days
FROM LIVE.silver_patients_dlt
GROUP BY hospital;
