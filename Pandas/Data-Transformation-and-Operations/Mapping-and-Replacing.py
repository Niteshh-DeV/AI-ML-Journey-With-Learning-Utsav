import pandas as pd

# Mapping and Replacing Values in Pandas

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Gender': ['F', 'M', 'M', 'M', 'F'],
    'Score': [85, 90, 78, 92, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
} # Sample Data

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Mapping means substituting each value in a Series with another value.

df['Grade'] = df['Score'].map(lambda x: 'A' if x >= 90 else 'B')
print("\nDataFrame after Mapping Scores to Grades:\n", df)

# Replacing Values

df['Gender'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)
print("\nDataFrame after Replacing Gender Codes:\n", df)