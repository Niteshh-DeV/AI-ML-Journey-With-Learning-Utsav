import pandas as pd
import matplotlib.pyplot as plt

# Data Visualization in pandas
# Pandas provides built-in methods for quick and easy data visualization using Matplotlib as the backend.
# This is useful for exploratory data analysis (EDA) to understand the distribution and relationships in the data.

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Age': [24, 27, 22, 32, 29, 24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Chicago', 'Houston'],
    'Score': [85, 90, 78, 92, 88, 85, 78, 92]
}

dataframe = pd.DataFrame(data)
print("Original DataFrame:\n", dataframe)

# Basic Plotting
# Line Plot

dataframe.plot(x='Name', y='Score', kind='line', title='Line Plot of Scores')
plt.show()

# Bar Plot
dataframe.plot(x='Name', y='Score', kind='bar', title='Bar Plot of Scores')
plt.show()
# Histogram
# Histogram shows the distribution of a single variable
dataframe['Score'].plot(kind='hist', title='Histogram of Scores', bins=5)
# bins specify the number of intervals
plt.show()

# Scatter Plot
dataframe.plot(x='Age', y='Score', kind='scatter', title='Scatter Plot of Age vs Score')
plt.show()

# Pie Chart
# Pie chart is useful for showing proportions of a whole
dataframe['City'].value_counts().plot(kind='pie', title='Pie Chart of City Distribution', autopct='%1.1f%%')
plt.show()
# autopct shows the percentage on the pie chart