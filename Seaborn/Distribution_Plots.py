import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = sns.load_dataset('tips')
print(data.head(10))

# Distribution Plot using Seaborn
# Distribution plots are used to visualize the distribution of a single variable.
# It includes histograms, kernel density estimation (KDE) plots, and rug plots.

# KDE Plot and Histogram using Seaborn
# KDE plots are used to estimate the probability density function of a continuous random variable.
# It shows the distribution of data over a continuous interval.

sns.set_style("whitegrid")
sns.set_palette("pastel")

sns.kdeplot(data['total_bill'], fill=True)

plt.title("Seaborn Distribution KDE Plot", fontsize=16)

plt.show()

# Histogram
sns.set_style("darkgrid")
sns.set_palette("bright")
sns.histplot(data['tip'], kde=True)
plt.title("Seaborn Distribution Histogram", fontsize=16)
plt.xlabel("Tip", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Rug Plot using Seaborn
# Rug plots are used to visualize the distribution of a single variable by drawing a small vertical line
# for each data point along the x-axis.
sns.set_style("ticks")
sns.set_palette("Set2")
sns.rugplot(data['size'], height=0.5)
plt.title("Seaborn Distribution Rug Plot", fontsize=16)
plt.xlabel("Size", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.show()