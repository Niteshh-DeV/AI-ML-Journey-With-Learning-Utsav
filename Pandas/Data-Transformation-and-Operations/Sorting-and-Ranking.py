import pandas as pd

# Sorting and Ranking in Pandas
# Pandas provides various methods to sort and rank data in Series and DataFrame.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
} # Sample Data

df = pd.DataFrame(data)
print("Original DataFrame:\n", df) 

# Sorting by Values

sorted_by_age = df.sort_values(by='Age') # Sort by Age in ascending order
print("\nDataFrame sorted by Age:\n", sorted_by_age)
# for decending order use ascending=False
decendind_name = df.sort_values(by='Name', ascending=False) # Sort by Name in descending order

# Sorting by Index
sorted_by_index = df.sort_index() # Sort by index in ascending order
print("\nDataFrame sorted by Index:\n", sorted_by_index)

# Ranking
# Ranking means assigning ranks to data points based on their values.
df['Age_Rank'] = df['Age'].rank() # Rank ages in ascending order
print("\nDataFrame with Age Ranks:\n", df)
