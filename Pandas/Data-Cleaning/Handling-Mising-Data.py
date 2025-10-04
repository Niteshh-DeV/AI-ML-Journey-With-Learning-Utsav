import pandas as pd

# Handling Missing Data in Pandas
# Missing data is a common issue in real-world datasets. Pandas provides several methods to handle missing data effectively.

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [24, None, 22, 32, 29],
    'City': ['New York', 'Los Angeles', None, 'Houston', 'Phoenix']
}

dataframe = pd.DataFrame(data)
print("Original DataFrame with Missing Data:\n", dataframe)

# Detecting Missing Data
print("\nDetecting Missing Data:")
print(dataframe.isnull())  # Returns a DataFrame of the same shape with boolean values
print(dataframe.isnull().sum())  # Count of missing values in each column
print(dataframe.notnull())  # Returns a DataFrame of the same shape with boolean values indicating non-missing values
# .notnull() is the opposite of .isnull()

# # .isna() and .notna() are similar to .isnull() and .notnull() respectively.
# print(dataframe.isna())  # Equivalent to isnull()
# print(dataframe.notna())  # Equivalent to notnull()

# To remove missing data we use dropna() 
removed_missing = dataframe.dropna()  # Drops any row with at least one missing value
print("\nDataFrame after Dropping Rows with Missing Data:\n", removed_missing)

removed_missing_columns = dataframe.dropna(axis=1) # axis=1 drops columns with at least one missing value
print("\nDataFrame after Dropping Columns with Missing Data:\n", removed_missing_columns)

# Filling Missing Data
filled_missing = dataframe.fillna({'Name': 'Unknown',
    'Age': dataframe['Age'].mean(),  # Fill missing Age with the mean age
    'City': 'Unknown'})  # Fill missing City with 'Unknown'
print("\nDataFrame after Filling Missing Data:\n", filled_missing)

#fillna() function is used to fill missing values in a DataFrame.
# It can take a scalar value, a dictionary, or a Series to fill the missing values
# You can also use methods like 'ffill' (forward fill) or 'bfill' (backward fill) to propagate non-missing values forward or backward.
# Example:
ffill_missing = dataframe.fillna(method='ffill')  # Forward fill 
print("\nDataFrame after Forward Filling Missing Data:\n", ffill_missing)
bfill_missing = dataframe.fillna(method='bfill')  # Backward fill
print("\nDataFrame after Backward Filling Missing Data:\n", bfill_missing)