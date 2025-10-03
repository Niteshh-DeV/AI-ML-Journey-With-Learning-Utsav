import pandas as pd
import numpy as np

#Series 
#Series in Pandas is a one-dimensional array-like object that can hold various data types, including integers, floats, strings, and Python objects. 
# It is similar to a column in a DataFrame or a one-dimensional array in NumPy.

my_Series = pd.Series([10, 20, 30, 40, 50])
print("Series:\n",my_Series)

Var1 = [1,2,3,4,5]
my_Series2 = pd.Series(Var1)
print("Series from List:\n",my_Series2)

# For custom indexing 

print("Custom Indexing:\n")
my_Series3 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(my_Series3)

# Accessing elements
print("Accessing Elements:\n")
print(my_Series3['a'])  # Accessing a single element by index label
print(my_Series3[['a', 'c', 'e']])  # Accessing multiple elements.

print(my_Series2.iloc[0])  # Accessing a single element by integer position
print(my_Series2.iloc[[0, 2, 4]])  # Accessing multiple elements by integer positions