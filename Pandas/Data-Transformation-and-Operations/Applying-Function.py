import pandas as pd

# Applying Functions to Data in Pandas
# Apply function is a powerful tool in Pandas that allows you to apply a function along an axis of the DataFrame (rows or columns) or on values in a Series.

data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 400]
} # Data with three columns A, B, and C

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Applying a function to each element in the DataFrame
#syntax: DataFrame.apply(func)

def square(x):
    return x ** 2

df_squared = df.map(square) # For element wise series wise operation
print("\nDataFrame after applying square function to each element:\n", df_squared)
# We use .apply(func) to apply a function along an axis of the DataFrame.
# By default, it applies the function to each column (axis=0). To apply it to each row, we set axis=1.

df_sum = df.apply(lambda x: x.sum(), axis=0) # For each column
df_row_sum = df.apply(lambda x: x.sum(), axis=1) # For each row 
 # Here lambda is an anonymous function that takes an input x and returns the sum of x.
 
print("\nSum of each column using apply:\n", df_sum)
print("\nSum of each row using apply:\n", df_row_sum)
