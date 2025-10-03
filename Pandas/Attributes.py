import pandas as pd

# Basic Attributes in Pandas

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series1 = pd.Series(list1)
print("Series:\n", series1)
print("Type of series1:", type(series1))

Dict = {
    'name' : ["Nitesh","Alice"],
    'age' : [25, 30],
    'city' : ["New York", "Los Angeles"]
}
df = pd.DataFrame(Dict)
print("DataFrame:\n", df)
print("Type of df:", type(df))

# head() and tail()

print(series1.head()) # First 5 elements
# print(series1.head(3)) # First 3 elements
print(df.head(2)) # First 2 rows of DataFrame

print(series1.tail()) # Last 5 elements
# print(series1.tail(2)) # Last 2 elements

# shape
print("Shape of series1:", series1.shape) # shape gives a tuple representing the dimensionality of the Series.
print ("Shape of df:", df.shape)

# size
print("Size of series1:", series1.size) # size returns the number of elements in the Series.
print("Size of df:", df.size)

# ndim
print("Number of dimensions of series1:", series1.ndim) # ndim returns the number
print ("Number of dimensions of df:", df.ndim) # of dimensions of the Series. For a Series, this will always be 1.


# columns
# Note: Series do not have columns attribute, only DataFrames do.

print("Columns of df:", df.columns) # columns returns the column labels of the DataFrame.

# index
print("Index of series1:", series1.index) # index returns the index (row labels) of the Series.
print("Index of df:", df.index) # index returns the index (row labels) of the DataFrame.


# info() and describe()
print("Info of df:")
df.info() # info() provides a concise summary of the DataFrame, including the index dtype, column dtypes, non-null values, and memory usage.
print("Description of df:")
print(df.describe()) # describe() generates descriptive statistics that summarize the central tendency, dispersion, and shape of a dataset's distribution, excluding NaN values.