# Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory (ADF)

## Objective

The objective of this assignment was to understand the fundamentals of Microsoft Azure Cloud and implement an end-to-end data pipeline using Azure Storage Account and Azure Data Factory (ADF).

## Tools and Services Used

* Microsoft Azure Portal
* Azure Resource Group
* Azure Storage Account
* Azure Blob Storage
* Azure Data Factory (ADF)
* Linked Services
* Source and Destination Datasets
* Get Metadata Activity
* Copy Data Activity
* IAM (Identity and Access Management)

## Dataset

**Superstore Dataset (CSV)**

## Implementation Steps

* Created an Azure Resource Group.
* Created an Azure Storage Account and Blob Container.
* Uploaded the Superstore CSV file to Blob Storage.
* Created an Azure Data Factory instance.
* Configured a Linked Service between ADF and Blob Storage.
* Created Source and Destination Datasets.
* Used the **Get Metadata** activity to validate the source file.
* Used the **Copy Data** activity to copy data from the source container to the destination container.
* Executed the pipeline using **Debug** and **Trigger Now**.
* Monitored pipeline execution through the ADF Monitor.
* Assigned the required IAM roles for secure access.

## Pipeline Workflow

```
Superstore CSV
      │
      ▼
Azure Blob Storage (Source)
      │
      ▼
Get Metadata Activity
      │
      ▼
Copy Data Activity
      │
      ▼
Azure Blob Storage (Destination)
```

## Output

The Azure Data Factory pipeline successfully copied the Superstore dataset from the source Blob Storage container to the destination container. The Get Metadata activity validated the file before execution, and the pipeline execution was successfully monitored through Azure Data Factory.

## Conclusion

This assignment provided hands-on understanding of Microsoft Azure services, including Azure Storage, Blob Storage, Azure Data Factory, Linked Services, Datasets, Get Metadata Activity, Copy Data Activity, IAM Roles, and the implementation of an end-to-end ETL data pipeline.

---

**Author:** Harshita Joshi
**Internship:** Celebal Technologies – Data Engineering Internship
