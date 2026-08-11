# import libraries
import pandas as pd

# read the dataset
df1= pd.read_csv(r'C:\Users\vijay\Downloads\Sample data (1).xlsx - Sheet1.csv')
print(df1.head())
print(df1.info())

# Check missing values
print(df1.isnull().sum())

# fill missing values with "None"
df1["Discount Band"] = df1["Discount Band"].fillna("None")
print(df1)

# drop duplicates
df1 = df1.drop_duplicates()
print(df1)

# Clean column names
df1.columns = df1.columns.str.strip()

# Calculate Profit Margin
df1["Profit Margin"] = (df1["Profit"].div(df1["Sales"].replace(0, pd.NA)).mul(100)).round(2)
print(df1)

# save the cleaned dataset to a new CSV file
df1.to_csv("cleaned_dataset(1).csv", index=False)