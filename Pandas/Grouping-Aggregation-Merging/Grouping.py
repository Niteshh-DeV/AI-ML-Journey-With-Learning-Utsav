import pandas as pd
# Grouping in Pandas

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
grouped_by_city = df.groupby('City')  # groupby() function is used to group data based on one or more columns.
# It returns a GroupBy object which can be further used for aggregation or transformation.
print("\nGrouped by City:\n", grouped_by_city)

# Iterating through groups
for city, group in grouped_by_city:
    print(f"\nCity: {city}\n", group)

# Viewing a specific group and group summary
print("\nGroup for City 'Chicago':\n", grouped_by_city.get_group('Chicago')) # .get_group() is used to retrieve a specific group from the GroupBy object.
print("\nGroup Summary (Size of each group):\n", grouped_by_city.size()) # .size() returns the size of each group.
