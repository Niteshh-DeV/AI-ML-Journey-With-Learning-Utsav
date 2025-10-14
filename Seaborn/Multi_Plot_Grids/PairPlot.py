import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = sns.load_dataset('iris')
print(data.head(10))

# Pair Plot using Seaborn
# Pair plots are used to visualize pairwise relationships in a dataset.
# It creates a grid of Axes such that each variable in the data will be shared across the y-axes across a single row and the x-axes across a single column.
sns.set_style("whitegrid")
sns.set_palette("Set1") # 'Set1' palette provides a set of bright colors
pair_plot = sns.pairplot(data, hue='species')
plt.suptitle("Seaborn Pair Plot (whitegrid + Set1)", fontsize=16, y=1.02) # y=1.02 moves the title up a bit
plt.xlabel("Features")
plt.ylabel("Features")

plt.show()