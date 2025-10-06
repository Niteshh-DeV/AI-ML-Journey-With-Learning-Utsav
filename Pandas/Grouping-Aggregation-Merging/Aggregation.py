import pandas as pd

# Aggregation in Pandas
# Aggregation refers to the process of summarizing or combining multiple values into a single value.

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Age': [24, 27, 22, 32, 29, 24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Chicago', 'Houston'],
    'Score': [85, 90, 78, 92, 88, 85, 78, 92]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Aggregating Data
mean_age = df['Age'].mean()  # Calculate mean age
sum_score = df['Score'].sum()  # Calculate total score
max_score = df['Score'].max()  # Find maximum score
min_age = df['Age'].min()  # Find minimum age
count_names = df['Name'].count()  # Count number of names
print("\nMean Age:", mean_age)
print("Total Score:", sum_score)
print("Maximum Score:", max_score)
print("Minimum Age:", min_age)
print("Count of Names:", count_names) 

# Aggregation with Grouping
grouped_by_city = df.groupby('City')  # Group data by City
mean_age_by_city = grouped_by_city['Age'].mean()  # Calculate mean age for each city


# .agg() method allows multiple aggregation operations at once.
agg_operations = grouped_by_city.agg({
    'Age': ['mean', 'min', 'max'],  # Mean, Min, Max of Age
    'Score': ['sum', 'mean']        # Sum and Mean of Score
})
print("agg_operations:\n", agg_operations)