import matplotlib.pyplot as plt
import numpy as np

# histogram is a graphical representation that organizes a group of data points into user-specified ranges.

# Sample data
x = np.random.randn(1000)
# randn is used to generate random numbers from a normal distribution

# Create a histogram
plt.hist(x, bins=20, color='blue', edgecolor='black', alpha=0.7)
# 'bins' is used to set the number of bins in the histogram, bins means the range of values

plt.title('Histogram Example', fontsize=14, fontweight='bold', color='purple')
plt.xlabel('Value', fontsize=12, color='blue')
plt.ylabel('Frequency', fontsize=12, color='blue')

plt.grid(axis='y', linestyle='--', linewidth=0.5)

plt.show()