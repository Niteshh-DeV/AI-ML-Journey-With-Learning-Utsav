import pandas as pd

#DataFrames
#DataFrame in Pandas is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). 
# It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

dataframe = pd.DataFrame(data)
print (dataframe)

# Accessing columns
print("Accessing Columns:")
print(dataframe['Name'])  # Accessing a single column
print(dataframe[['Name', 'Age']])  # Accessing multiple columns

# Accessing rows
print("Accessing Rows:")
print(dataframe.iloc[0])  # Accessing the first row by index
print(dataframe.loc[1])   # Accessing the second row by label

# Here .ilok and .loc are used to access rows in a DataFrame.
# .iloc is primarily integer position based (from 0 to length-1 of the axis), 
# while .loc is primarily label based, but may also be used with a boolean array
# The main difference between .iloc and .loc is that .iloc is used for integer-location based indexing,
# while .loc is used for label-based indexing.
