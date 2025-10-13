import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = sns.load_dataset('tips')
print(data.head(10))


# Relational Plot using Seaborn
# Relational plots are used to visualize the relationship between two variables, often with additional dimensions represented by color and size.

sns.set_style("whitegrid") 
sns.set_palette("pastel") # pastel palette provides a set of soft, light colors
rel_plot = sns.relplot(x='total_bill', y='tip', hue='day', size='size', sizes=(20, 200), data=data) 
 # size = 'size' sets the size of points based on the 'size' variable, 
 # hue = 'day' sets the color of points based on the 'day' variable
 # sizes=(20, 200) sets the minimum and maximum size of the points

plt.suptitle("Seaborn Relational Plot (whitegrid + pastel)", y=1.03) # y=1.03 moves the title up a bit
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.savefig("Seaborn_Relational_Plot.png") # Save the figure
plt.show()

# The difference between scatterplot and relational plot is that scatterplot is used to visualize the relationship between two continuous variables,
# while relational plot can visualize the relationship between two continuous variables with additional dimensions represented by color and size.
# In other words, relational plot is a more general form of scatterplot that can include additional information through the use of hue and size parameters.
sns.set_style("dark")
sns.set_palette("bright") # bright palette provides a set of bright, vibrant colors
sns.relplot(x='total_bill', y='tip', hue='sex', style='time', size='size', data=data)
plt.title("Relational Plot with Different Styles and Hues")
plt.show()