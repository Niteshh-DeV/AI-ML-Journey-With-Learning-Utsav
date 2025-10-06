import pandas as pd

# Filtering groups in Pandas

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Age': [24, 27, 22, 32, 29, 24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Chicago', 'Houston'],
    'Score': [85, 90, 78, 92, 88, 85, 78, 92]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Grouping Data
grouped_by_city = df.groupby('City')
print("\nGrouped by City:\n", grouped_by_city)

# Filtering Groups
# Filtering allows you to filter out groups based on a condition.
# For example, we can filter cities where the average score is greater than 85.
filtered_groups = grouped_by_city.filter(lambda x: x['Score'].mean() > 85)
print("\nFiltered Groups (Cities with average Score > 85):\n", filtered_groups)
# The filter() function applies a function to each group and retains only those groups for which the function returns True.

# Another example: Filter groups where the number of members in the group is greater than 1.
filtered_by_size = grouped_by_city.filter(lambda x: len(x) >= 2)
print("\nFiltered Groups (Cities with more than 1 members):\n", filtered_by_size)