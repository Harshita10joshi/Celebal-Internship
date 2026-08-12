# Power BI Dashboard Specification

## Data source
Connect Power BI to the Gold Delta tables from Databricks SQL Warehouse:
- gold_patient_statistics
- gold_hospital_statistics
- gold_condition_statistics
- gold_admission_statistics
- gold_insurance_statistics

## Page 1 — Healthcare Overview
Cards:
- Total Patient Records
- Total Hospitals
- Total Doctors
- Total Billing
- Average Billing
- Average Length of Stay

Charts:
- Patients by Hospital
- Patients by Medical Condition
- Patients by Admission Type

## Page 2 — Hospital Performance
- Top 10 Hospitals by Patient Count
- Hospital ranking table
- Average Billing by Hospital
- Total Billing by Hospital

## Page 3 — Condition & Insurance Analysis
- Patient count by medical condition
- Billing by medical condition
- Patient count by insurance provider
- Billing by insurance provider

## Suggested slicers
- Medical Condition
- Gender
- Admission Type
- Insurance Provider
- Hospital
- Test Results
