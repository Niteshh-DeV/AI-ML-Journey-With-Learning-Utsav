import pandas as pd

# Changing Data Types in Pandas
# Changing data types is often necessary for data analysis and manipulation. Pandas provides several methods to change the data types of columns in a DataFrame.

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': ['24', '27', '22', '32'],  # Age as strings
    'Salary': [50000.0, 60000.0, 55000.0, 70000.0],  # Salary as floats
    'Is_Employed': ['True', 'False', 'True', 'True']  # Booleans as strings
}   # Sample data with different data types

dataframe = pd.DataFrame(data)
print("Original DataFrame:\n", dataframe)

# Checking Data Types
print("\nData Types of the DataFrame:\n", dataframe.dtypes)

# Changing Data Types
# To change the data type of a column, we use the astype() method.

dataframe['Age'] = dataframe['Age'].astype(int)  # Change Age from string to integer
dataframe['Salary'] = dataframe['Salary'].astype(int)  # Change Salary from float to integer
dataframe['Is_Employed'] = dataframe['Is_Employed'].astype(bool)  # Change Is_Employed from string to boolean

print("\nDataFrame after Changing Data Types:\n", dataframe)
print("\nData Types after Changing:\n", dataframe.dtypes)