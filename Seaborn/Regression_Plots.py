import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = sns.load_dataset('iris')
print(data.head(10))

# Regression Plots 
# Regression plots are used to visualize the relationship between a dependent variable and one or more independent variables, often with a regression line to show the trend.

sns.set_style("whitegrid")
sns.set_palette("muted") # muted palette provides a set of soft, muted colors

reg_plot = sns.regplot(x='sepal_length', y='petal_length', data=data)
# regplot creates a scatter plot with a regression line
# x = 'sepal_length' is the independent variable
# y = 'petal_length' is the dependent variable
plt.title("Seaborn Regression Plot (whitegrid + muted)")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig("Seaborn_Regression_Plot.png") # Save the figure
plt.show()

#lmplot is another way to create regression plots, which can also include a hue parameter to show different regression lines for different categories.
sns.set_style("dark")
sns.set_palette("dark") # dark palette provides a set of dark, rich colors
sns.lmplot(x='sepal_length', y='petal_length', hue='species', data=data)
# lmplot creates a scatter plot with regression lines for each species
# hue = 'species' sets different colors and regression lines for each species
plt.title("Seaborn LM Plot with Different Species")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig("Seaborn_LM_Plot.png") # Save the figure
plt.show()

# Residue plot is used to visualize the residuals of a regression model, which helps to assess the goodness of fit.
# It shows the difference between the observed and predicted values.
sns.set_style("ticks")
sns.set_palette("colorblind") # colorblind palette provides a set of colors that are distinguish
sns.residplot(x='sepal_length', y='petal_length', data=data)
# residplot creates a plot of residuals
plt.title("Seaborn Residue Plot (ticks + colorblind)")
plt.xlabel("Sepal Length")
plt.ylabel("Residuals of Petal Length")

plt.show()