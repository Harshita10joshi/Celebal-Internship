# Week 8 – E-Commerce Order Analytics System

## Objective

Design and develop an end-to-end e-commerce data analytics system using Python, Pandas, and SQL to process, clean, validate, and analyze order data and generate meaningful business insights.

## Project Overview

This project implements a complete data analytics pipeline for e-commerce order data. Realistic datasets are generated with intentional inconsistencies such as duplicate records, missing values, invalid prices, inconsistent categories, invalid customer references, and invalid quantities.

The raw data is cleaned and validated using Pandas and then stored in a MySQL database for further analysis. Advanced SQL queries are used to generate business insights related to revenue, customers, products, customer segmentation, cohort analysis, and retention.

A command-line reporting tool is also implemented to generate dynamic reports from the database.

## Technologies Used

- Python
- Pandas
- Faker
- MySQL
- SQL
- MySQL Connector
- Command Line Interface (CLI)

## Project Structure

```text
Week 8/
└── E-Commerce-Order-Analytics-System/
    │
    ├── data/
    │   ├── raw/
    │   └── cleaned/
    │
    ├── python/
    │   ├── generate_data.py
    │   ├── data_cleaning.py
    │   ├── validation.py
    │   ├── import_data_to_mysql.py
    │   └── reporting_tool.py
    │
    ├── sql/
    │   ├── create_tables.sql
    │   └── analytics_queries.sql
    │
    ├── reports/
    │   └── business_report.md
    │
    ├── requirements.txt
    └── README.md
