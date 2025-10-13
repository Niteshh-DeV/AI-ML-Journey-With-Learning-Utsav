import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')
print(tips.head(8))

# Categorical Plot (catplot) using Seaborn
# Categorical plots are used to visualize the distribution of a categorical variable or the relationship between a categorical variable and a numerical variable.
# It includes box plots, violin plots, bar plots, point plots, strip plots, swarm plots, etc.

sns.set_style("whitegrid")
sns.set_palette("Set2") # 'Set2' palette provides a set of pastel colors

# Catplot
sns.catplot(x='day', y='total_bill', kind='box', data=tips, height=5, aspect=1.5)
# 'kind' specifies the type of categorical plot, here we are using 'box' for box plot
# 'height' and 'aspect' control the size of the plot

plt.title("Seaborn Categorical Plot (Box Plot)", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill", fontsize=12)
plt.ylim(0, 60) # Set y-axis limits for better visualization
plt.show()

# Violin Plot using Seaborn
# Violin plots are similar to box plots, but they also show the kernel density estimation of the data.
# The width of the violin represents the density of the data at different values.
# And center line represents the median of the data.

sns.set_style("darkgrid")
sns.set_palette("pastel")
sns.catplot(x='day', y='total_bill', kind='violin', data=tips, aspect=1.5)
plt.title("Seaborn Categorical Plot (Violin Plot)", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill", fontsize=12)
plt.ylim(0, 60)
plt.show()

# Swarm Plot using Seaborn
# Swarm plots are similar to strip plots, but they adjust the positions of the points to avoid overlap.
# This makes it easier to see the distribution of the data points.

sns.set_style("ticks")
sns.set_palette("bright")
sns.catplot(x='day', y='total_bill', kind='swarm', data=tips, height=5, aspect=1.5)
plt.title("Seaborn Categorical Plot (Swarm Plot)", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill", fontsize=12)
plt.show()
