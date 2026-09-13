# Data Cleaning – Titanic Dataset

## Project Overview

This project demonstrates professional data cleaning using Python, Pandas, NumPy, and Jupyter Notebook.

The Titanic dataset was cleaned and transformed into an analysis-ready dataset by identifying and handling missing values, duplicate records, inconsistent formatting, outliers, and incorrect data types.

## Dataset

Dataset: Titanic Passenger Dataset

Original Dataset:
- Rows: 891
- Columns: 12

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Data Cleaning Steps

### 1. Data Quality Report

Created a data quality report containing:
- Missing values
- Missing percentage
- Data types
- Duplicate records
- Numerical value ranges

### 2. Missing Value Handling

- Age: Missing values were replaced using median imputation.
- Embarked: Missing values were replaced using mode imputation.
- Cabin: Missing values were replaced with "Unknown".

### 3. Duplicate Removal

Duplicate records were identified and removed.

The original dataset contained 0 duplicate rows.

### 4. Data Standardization

- Sex values were standardized to consistent title case.
- Embarked values were standardized to uppercase.
- Extra spaces were removed.

### 5. Outlier Detection

The IQR method was used to identify outliers in numerical columns such as:
- Age
- SibSp
- Parch
- Fare

Detected outliers were retained because they may represent valid passenger records.

### 6. Data Type Correction

Data types were corrected for:
- PassengerId
- Survived
- Pclass
- Age
- SibSp
- Parch
- Fare

### 7. Before vs After Cleaning

| Measure | Before Cleaning | After Cleaning |
|---|---:|---:|
| Rows | 891 | 891 |
| Columns | 12 | 12 |
| Duplicate Rows | 0 | 0 |
| Missing Values | 866 | 0 |

## Output

The cleaned dataset was saved as:

`Titanic_Cleaned.csv`

## Conclusion

The Titanic dataset was successfully cleaned and converted into an analysis-ready dataset. Missing values were handled using appropriate imputation strategies, duplicate records were checked, categorical values were standardized, outliers were detected using the IQR method, and data types were corrected.
