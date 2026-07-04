# Week 3 - SQL Sales Data Analysis using Subqueries, CTEs, and Window Functions

## Project Overview

This project analyzes the Superstore sales dataset using advanced SQL concepts. The dataset was imported into MySQL, normalized into separate tables, and analyzed to solve different business-related problems using Subqueries, Common Table Expressions (CTEs), Window Functions, and JOIN operations.

---

## Objective

- Import the Superstore dataset into MySQL.
- Create normalized tables: Customers, Products, and Orders.
- Perform sales analysis using SQL.
- Apply Subqueries, CTEs, Window Functions, and JOINs.
- Generate meaningful business insights from the sales data.

---

## Dataset

- **Dataset Name:** Sample Superstore Dataset
- **Source:** Kaggle
- **Database:** MySQL
- **Raw Table:** `superstore_raw`

---

## Database Tables

The dataset was divided into the following tables:

- **customers**
- **products**
- **orders**

---

## SQL Concepts Used

- SELECT Statements
- Aggregate Functions (`SUM`, `AVG`, `MAX`)
- GROUP BY
- HAVING
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
  - ROW_NUMBER()
  - RANK()
- INNER JOIN
- Date Conversion using `STR_TO_DATE()`

---

## Business Problems Solved

- Find orders with sales above the average sales.
- Find the highest-value order for each customer.
- Calculate total sales for each customer using CTE.
- Display customer names with their total sales.
- Rank customers based on total sales.
- Identify the top-performing customers.
- Find customers who placed only one order.
- Find customers whose total sales are above the average customer sales.

---

## Key Insights

- Successfully normalized the raw dataset into relational tables.
- Used Subqueries to identify above-average sales.
- Applied CTEs to simplify customer-wise sales aggregation.
- Used Window Functions to rank customers based on sales performance.
- Combined JOIN, CTE, and Window Functions to generate meaningful business reports.

---

## Technologies Used

- MySQL Workbench
- SQL
- Kaggle Superstore Dataset

---

## Project Files

```
Week-3/
│── README.md
│── week3_sales_analysis.sql
│── screenshots/
```

---

## Learning Outcomes

Through this project, I learned how to:

- Import and normalize raw datasets.
- Use Subqueries for analytical queries.
- Apply CTEs to simplify complex SQL queries.
- Use Window Functions for ranking and reporting.
- Solve real-world business problems using SQL.

---

## Conclusion

This project demonstrates how advanced SQL techniques can be used to analyze sales data and generate valuable business insights. It strengthened my understanding of SQL querying, data analysis, and database management.
