import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn is a statistical data visualization library built on top of Matplotlib. 
# It provides a high-level interface for drawing attractive and informative statistical graphics.

# Seaborn has built in datasets for practice and demonstration purposes.
# for eg , 'tips' dataset , 'iris' dataset etc.

# Working with the 'tips' dataset
tips = sns.load_dataset('tips')
print(type(tips)) 
# Here tips is a pandas DataFrame Hence we can use all pandas functions on it.

print("Tips Dataset:\n", tips.head())

# Basic Plotting with Seaborn

sns.lineplot(data=tips.head(10), x='total_bill', y='tip', marker='o', color='orange')
plt.title('Line Plot of Total Bill vs Tip')
plt.show()

sns.barplot(data=tips, x='day', y='total_bill', ci=None, palette='coolwarm') # ci=None removes the confidence interval ie error bars
plt.title('Bar Plot of Total Bill by Day')
plt.show()