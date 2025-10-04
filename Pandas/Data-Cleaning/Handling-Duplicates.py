import pandas as pd

# Handling Duplicates in Pandas

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob'],
    'Age': [24, 27, 22, 24, 32, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Houston', 'Los Angeles']
}  # Sample data with duplicates

dataframe = pd.DataFrame(data)
print("Original DataFrame with Duplicates:\n", dataframe)

# Detecting Duplicates
# For detecting duplicates, we use the duplicated() method.
print("\nDetecting Duplicates:")
print(dataframe.duplicated())  # Returns a boolean Series indicating duplicate rows
print(dataframe.duplicated(keep=False))  # Marks all duplicates as True
print(dataframe.duplicated(subset=['Name', 'Age']))  # Check duplicates based on specific columns

# Removing Duplicates
# To remove duplicates, we use the drop_duplicates() method.

print("\nDataFrame after Dropping Duplicates:")
removed_duplicates = dataframe.drop_duplicates()  # Drops duplicate rows, keeping the first occurrence
print(removed_duplicates)
removed_duplicates_last = dataframe.drop_duplicates(keep='last')  # Keeps the last occurrence of duplicates
print("\nDataFrame after Dropping Duplicates (keeping last occurrence):")
print(removed_duplicates_last)