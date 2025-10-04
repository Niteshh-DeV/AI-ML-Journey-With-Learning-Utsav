import pandas as pd

# Renaming and Reordering in Pandas

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

dataframe = pd.DataFrame(data)  
print("Original DataFrame:\n", dataframe)

# Renaming Columns
# To rename columns, we use the rename() method.

renamed_df = dataframe.rename(columns={'Name': 'Full Name', 'Age': 'Age in Years'})
print("\nDataFrame after Renaming Columns:\n", renamed_df)

# Reordering Columns
# To reorder columns, we can simply specify the new order of columns.
reordered_df = dataframe[['City', 'Name', 'Age']]
print("\nDataFrame after Reordering Columns:\n", reordered_df)

# We also can use the reindex() method to reorder columns.
reindexed_df = dataframe.reindex(columns=['Age', 'City', 'Name'])
print("\nDataFrame after Reindexing Columns:\n", reindexed_df)