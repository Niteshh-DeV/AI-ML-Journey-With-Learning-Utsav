import pandas as pd

# Basic Opeations in Pandas

# Filtering
data = {
    'Name': ['Alice','Eva', 'Bob', 'Zara', 'David'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print(filtered_df)

# Sorting
sorted_df = df.sort_values(by='Name') # Sort by Name in ascending order
print("Sorted DataFrame by Name:\n", sorted_df)
# sort index
sorted_index_df = df.sort_index(ascending=False) # Sort by index in descending order
print("Sorted DataFrame by Index:\n", sorted_index_df)

# Adding a new column
df['Salary'] = [50000, 60000, 55000, 70000, 65000]
print("DataFrame with new Salary column:\n", df)    

# Dropping a column
df_dropped = df.drop(columns=['City'])
print("DataFrame after dropping City column:\n", df_dropped)