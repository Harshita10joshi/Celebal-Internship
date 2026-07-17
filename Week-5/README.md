# Spark Fundamentals & Data Processing Assignment

## 📌 Objective

The objective of this assignment is to understand Apache Spark fundamentals and perform data cleaning, filtering, transformations, schema modifications, and aggregations using Spark DataFrames.

---

## 🛠️ Technologies Used

- Apache Spark
- PySpark
- Python
- Google Colab / Jupyter Notebook

---

## 📂 Dataset

A sample sales dataset was created for this assignment containing the following fields:

- user_id
- transaction_date
- region
- product_category
- sale_amount
- city
- status
- age
- subscription
- email
- username
- raw_timestamp
- price
- store_id

The dataset intentionally includes:
- Duplicate records
- Null values
- Empty strings
- Different regions and product categories

to demonstrate data cleaning and transformation operations.

---

## 📖 Assignment Topics Covered

### Spark Fundamentals
- Limitations of MapReduce
- Advantages of Apache Spark
- In-Memory Computing
- Spark DataFrames
- DataFrame Immutability
- Shuffle Operations

### Data Cleaning
- Removing Duplicate Records
- Handling Null Values
- Filling Missing Values
- Removing Invalid Records

### Data Transformation
- Filtering Records
- GroupBy Operations
- Aggregations
- Schema Modification
- Casting Data Types
- Renaming Columns

### Aggregations
- Count
- Sum
- Average
- Minimum
- Maximum

---

## ✅ Tasks Performed

- Removed duplicate rows using `dropDuplicates()`
- Filled null values using `na.fill()`
- Filtered records using multiple conditions
- Calculated average sales by category
- Counted records grouped by city
- Calculated minimum, maximum and average price
- Converted timestamp column to `TimestampType`
- Removed invalid email and username records
- Built a complete data cleaning and aggregation pipeline

---

## 📊 Key Spark Concepts Demonstrated

- Spark DataFrames
- Transformations
- Actions
- Wide Transformations
- Shuffle
- Lazy Evaluation
- In-Memory Processing
- Data Cleaning
- Aggregation
- Schema Handling

---

## 📁 Project Structure

```
Spark_Assignment/
│
├── Celebal_Spark_Assignment_Complete.ipynb
└── README.md
```

---

## 🎯 Learning Outcomes

After completing this assignment, I learned how to:

- Work with Spark DataFrames
- Clean real-world datasets
- Handle missing and duplicate values
- Apply filtering and aggregation operations
- Modify DataFrame schemas
- Understand Spark's execution model
- Build a complete data processing pipeline

---

## 👩‍💻 Author

**Harshita Joshi**

B.Tech Computer Science Engineering

DIT University

Data Engineer Intern – Celebal Technologies
