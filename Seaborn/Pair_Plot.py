import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Pair Plot using Seaborn
# Pair plots are used to visualize pairwise relationships in a dataset.
# It creates a grid of Axes such that each variable in the data will be shared across the y-axes across a single row and the x-axes across a single column.

sns.set_style("whitegrid")
sns.set_palette("Set1") # 'Set1' palette provides a set of bright colors
pair_plot = sns.pairplot(tips, hue='sex')
plt.suptitle("Seaborn Pair Plot", fontsize=16, y=1.02) # y=1.02 moves the title up a bit

plt.savefig("Seaborn_Pair_Plot.png") # Save the figure
plt.show()