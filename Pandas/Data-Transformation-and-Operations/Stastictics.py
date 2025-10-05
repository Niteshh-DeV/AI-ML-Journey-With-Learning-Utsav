import pandas as pd

# Stastictics And Mathematics

data = {
    'Name': ['Nitesh', 'Aarav', 'Sita', 'Ramesh', 'Ravi'],
    'Math': [85, 78, 92, 65, 88],
    'Science': [80, 75, 90, 70, 85],
    'English': [82, 77, 95, 68, 84]
}

df = pd.DataFrame(data)

df['marks'] = df[['Math', 'Science', 'English']].sum(axis=1)

print("Data:")
print(df, "\n")

# mean
mean_marks = df['marks'].mean()
print(f"Average Marks: {mean_marks:.2f}")

# Standard Deviation
std_marks = df['marks'].std()
print(f"Standard Deviation: {std_marks:.2f}")

#S um
df['Math+Science'] = df[['Math', 'Science']].sum(axis=1)
print("\nTotal of Math + Science for each student:")
print(df[['Name', 'Math+Science']])

# Correletion
print("\nCorrelation between subjects:")
print(df[['Math', 'Science', 'English', 'marks']].corr())