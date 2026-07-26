# Final Spark Assignment

## Objective

The objective of this assignment is to understand Apache Spark architecture and perform efficient data processing using PySpark. The assignment demonstrates reading data, applying transformations, filtering records, handling schemas and null values, comparing file formats, and writing processed data into optimized storage formats.

---

## Technologies Used

- Apache Spark
- PySpark
- Python
- Jupyter Notebook

---

## Topics Covered

- Spark Architecture (Driver, Cluster Manager, Executors)
- Lazy Evaluation
- Directed Acyclic Graph (DAG)
- Schema Handling
- DataFrame Transformations
- Filtering and Column Selection
- Renaming Columns
- Adding New Columns
- Handling Null Values
- Wide Transformations (Shuffle)
- Predicate Pushdown
- CSV vs Parquet
- Spark Best Practices

---

## Project Structure

```
Final_Spark_Assignment/
│── Final_Spark_Assignment.ipynb
│── spark_assignment.py
│── input/
│     └── employees.csv
│── output_csv/
│── output_parquet/
└── README.md
```

---

## Steps Performed

### 1. Created Spark Session

Initialized Spark using `SparkSession`.

### 2. Defined Schema

Created an explicit schema instead of using schema inference for better performance.

### 3. Read CSV File

Loaded the employee dataset using the predefined schema.

### 4. Selected Required Columns

Selected only the necessary columns for processing.

### 5. Modified DataFrame

- Renamed Salary column to MonthlySalary
- Converted Department names to uppercase
- Added necessary transformations

### 6. Filtered Records

Filtered employees whose salary is greater than **50000**.

### 7. Handled Null Values

Removed null records using `na.drop()`.

### 8. Saved Output

Stored processed data in both:

- CSV
- Parquet

---

## Spark Architecture

### Driver

- Creates Spark Session
- Builds execution plan
- Schedules tasks

### Cluster Manager

- Allocates resources
- Manages executors

### Executors

- Execute tasks
- Store intermediate data
- Return results to the Driver

---

## Lazy Evaluation

Spark does not execute transformations immediately.

Instead, it creates a Directed Acyclic Graph (DAG) and waits until an action like `show()` or `write()` is called. This optimization improves performance by minimizing unnecessary computations.

---

## Wide Transformations

Operations like:

- groupBy()
- join()

are called **wide transformations** because they require data movement between executors (Shuffle), making them more expensive than narrow transformations.

---

## Predicate Pushdown

When using Parquet files, Spark reads only the required rows and columns instead of scanning the entire dataset.

This optimization significantly improves query performance.

---

## CSV vs Parquet

| CSV | Parquet |
|------|----------|
| Row-based storage | Column-based storage |
| Larger file size | Smaller file size |
| Slower performance | Faster performance |
| No compression | Compressed |
| No schema storage | Schema stored |
| No predicate pushdown | Supports predicate pushdown |

---

## Best Practices

- Define schema explicitly.
- Filter data as early as possible.
- Avoid unnecessary shuffle operations.
- Use Parquet for large datasets.
- Avoid using `collect()` on large datasets.
- Use `show()` for displaying results.
- Select only required columns.

---

## Performance Insights

- Spark uses Lazy Evaluation to optimize execution.
- DAG minimizes unnecessary computations.
- Parquet provides better performance than CSV.
- Explicit schema improves reading speed.
- Early filtering reduces processing time.
- Wide transformations trigger Shuffle and should be minimized.

---

## Conclusion

This assignment demonstrates the complete Spark data processing pipeline:

**Read → Transform → Filter → Handle Null Values → Write**

It also covers Spark architecture, Lazy Evaluation, DAG optimization, schema handling, DataFrame transformations, and performance optimization techniques using PySpark.
