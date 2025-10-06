import pandas as pd

# Combining DataFrames in Pandas
# Pandas provides several methods to combine DataFrames, including concat(), merge(), and join()

# Sample DataFrames
data1 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
}
data2 = {
    'ID': [4, 5, 6],
    'Name': ['David', 'Eve', 'Frank']
}
data3 = {
    'ID': [1, 2, 3],
    'Score': [85, 90, 78]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Concatenating DataFrames
# The concat() function is used to concatenate DataFrames along a particular axis (rows or columns).
concatenated_df = pd.concat([df1, df2], ignore_index=True) # ignore_index=True resets the index in the concatenated DataFrame.
print("Concatenated DataFrame:\n", concatenated_df)

# Merging DataFrames
# The merge() function is used to merge DataFrames based on a common column (like SQL JOIN).
merged_df = pd.merge(df1, df3, on='ID') # Merging df1 and df3 on the 'ID' column.
print("\nMerged DataFrame:\n", merged_df)

# Joining DataFrames
# The join() function is used to join DataFrames based on their index or a key column.
df1.set_index('ID', inplace=True) # Setting 'ID' as index for df1
df3.set_index('ID', inplace=True) # Setting 'ID' as index for df3
joined_df = df1.join(df3, how='inner') # Joining df1 and df3 on their index.
print("\nJoined DataFrame:\n", joined_df)
# The how parameter can be 'left', 'right', 'outer', or 'inner' to specify the type of join. Inner join returns only the matching rows.