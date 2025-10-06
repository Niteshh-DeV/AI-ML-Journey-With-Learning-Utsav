import pandas as pd

# Transforming Grouped Data in Pandas
# Transformring means applying a function to each group and returning a DataFrame with the same shape as the original.
# This is useful when you want to perform operations on groups but still retain the original DataFrame structure.

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Age': [24, 27, 22, 32, 29, 24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Chicago', 'Houston'],
    'Score': [85, 90, 78, 92, 88, 85, 78, 92]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Grouping Data
grouped_by_city = df.groupby('City')
print("\nGrouped by City:\n", grouped_by_city)

# Transforming Groups
# For example, we can standardize the 'Age' within each city group.

standardized_age = grouped_by_city['Age'].transform(lambda x: (x - x.mean()) / x.std())
df['Standardized_Age'] = standardized_age
print("\nDataFrame after Standardizing Age within each City:\n", df)

