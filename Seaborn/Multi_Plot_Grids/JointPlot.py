import seaborn as sns
import matplotlib.pyplot as plt

# Load iris dataset
data = sns.load_dataset('iris')
print(data.head(10))

# Joint Plot using Seaborn
# Joint plots are used to visualize the relationship between two variables along with their individual distributions.
# It combines a scatter plot (or other bivariate plot) with univariate plots (histograms or density plots) on the axes.
sns.set_style("whitegrid")
sns.set_palette("deep") # 'deep' palette provides a set of deep, rich colors
joint_plot = sns.jointplot(x='sepal_length', y='petal_length', data=data, kind='reg', color='g')
# kind='reg' adds a regression line to the scatter plot
# x = 'sepal_length' is the independent variable
# y = 'petal_length' is the dependent variable
plt.suptitle("Seaborn Joint Plot (whitegrid + deep)", fontsize=16, y=1.02) # y=1.02 moves the title up a bit
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig("Seaborn_Joint_Plot.png") # Save the figure
plt.show()