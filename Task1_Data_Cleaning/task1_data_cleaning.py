import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("train.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())
