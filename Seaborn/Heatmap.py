import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load dataset
data = sns.load_dataset('tips')
print(data.head(10))

# Heatmap using Seaborn
# Heatmaps are used to visualize data in a matrix format, where individual values are represented as colors.
# They are useful for visualizing correlation matrices, frequency tables, and other types of data that can be represented in a grid format.

# Create a pivot table for the heatmap
pivot_table = data.pivot_table(values='total_bill', index='day', columns='time', aggfunc='mean', observed=True)
print(pivot_table)

sns.set_style("whitegrid")
sns.set_palette("coolwarm") # 'coolwarm' palette provides a gradient from cool to
heat = sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap='coolwarm', cbar=True, linewidths=.5)
# annot=True adds the numerical values to each cell
# cmap='coolwarm' sets the color map for the heatmap
# cbar=True adds a color bar to the side of the heatmap
# linewidths=.5 adds lines between the cells for better visibility
plt.title("Seaborn Heatmap (whitegrid + coolwarm)", fontsize=16)
plt.xlabel("Time of Day", fontsize=12)
plt.ylabel("Day of the Week", fontsize=12)
plt.show()

# Correlation Matrix Heatmap
# A correlation matrix heatmap is used to visualize the correlation coefficients between multiple variables in a dataset.
# The values range from -1 to 1, where 1 indicates a perfect positive correlation
# for correlation matrix we need numerical data only
numeric_data = data.select_dtypes(include=['float64', 'int64'])
corr = numeric_data.corr()
print(corr)
sns.set_style("dark")
sns.set_palette("viridis") # 'viridis' palette provides a gradient from dark purple
sns.heatmap(corr, annot=True, fmt=".2f", cmap='viridis', cbar=True, linewidths=.5)
plt.title("Correlation Matrix Heatmap (dark + viridis)", fontsize=16)
plt.show()
