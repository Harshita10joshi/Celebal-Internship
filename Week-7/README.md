# Python Basics and Data Exploration using Pandas

## Objective
The objective of this assignment is to learn Python basics and perform data exploration and cleaning using the Pandas library.

---

## Dataset
- **Dataset:** Superstore Dataset
- **Source:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

---

## Tools & Technologies
- Python 3
- Pandas
- Jupyter Notebook / Google Colab

---

## Tasks Performed

### 1. Load Dataset
- Loaded the CSV dataset into a Pandas DataFrame using `pd.read_csv()`.

### 2. Data Exploration
- Displayed the first and last five records.
- Checked dataset shape.
- Viewed column names.
- Examined data types.
- Displayed dataset information.

### 3. Handle Missing Values
- Identified missing values using `isnull().sum()`.
- Filled missing numerical values with the median.
- Filled missing categorical values with the mode.

### 4. Basic Data Operations
- Selected required columns.
- Filtered rows based on conditions.

### 5. Remove Duplicates
- Removed duplicate records using `drop_duplicates()`.

### 6. Create Derived Column
- Created a new column named **total_amount**.

```
total_amount = Price × Quantity
```

*(For the Superstore dataset, the `Sales` column can be used if a `Price` column is unavailable.)*

### 7. Save Cleaned Dataset
- Saved the cleaned DataFrame as:

```
cleaned_superstore.csv
```

---

## Project Structure

```
Python-Pandas-Assignment/
│── Python_Pandas_Assignment.ipynb
│── SampleSuperstore.csv
│── cleaned_superstore.csv
└── README.md
```

---

## Output
- Data successfully loaded and explored.
- Missing values handled.
- Duplicate records removed.
- Derived column created.
- Cleaned dataset saved as a new CSV file.

---

## Learning Outcomes
- Understanding of Python basics.
- Working with Pandas DataFrames.
- Data exploration techniques.
- Handling missing values.
- Data filtering and selection.
- Removing duplicate records.
- Creating new columns.
- Exporting cleaned datasets.

---

## Author

**Harshita Joshi**
