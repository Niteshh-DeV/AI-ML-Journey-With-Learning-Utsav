import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')
# 'tips' dataset contains information about the tips received by waitstaff in a restaurant.

# Create a boxplot
sns.boxplot(x='day', y='total_bill', data=tips, palette='Set3')
# 'x' is used to set the categorical variable on the x-axis
# 'y' is used to set the numerical variable on the y-axis
# 'palette' is used to set the color palette for the boxes

plt.title('Boxplot of Total Bill by Day', fontsize=14, fontweight='bold', color='purple')
sns.despine()  # Remove the top and right spines for a cleaner look
sns.set_style('whitegrid')  # Set the background style to white grid
plt.xlabel('Day of the Week', fontsize=12, color='blue')
plt.ylabel('Total Bill', fontsize=12, color='blue')

plt.show()