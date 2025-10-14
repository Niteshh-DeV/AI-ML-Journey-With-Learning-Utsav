import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

# Load dataset
data = sns.load_dataset('iris')

# Facet Grid using Seaborn
# Facet grids are used to create a grid of plots based on the values of one or more categorical variables.
# It allows for easy comparison of distributions or relationships across different subsets of the data

sns.set_style("whitegrid")
sns.set_palette("Set3") # 'Set3' palette provides a set of pastel colors
facet = sns.FacetGrid(data, col='species')
# col='species' creates a separate column for each species in the dataset
facet.map(sns.scatterplot, 'sepal_length', 'petal_length')
# map() applies the scatterplot function to each subset of the data
plt.suptitle("Seaborn Facet Grid (whitegrid + Set3)", y=1.05) # y=1.05 moves the title up a bit
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig("Seaborn_Facet_Grid.png") # Save the figure
plt.show()
