import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.random.rand(50)
y = np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o', s=100, alpha=0.7, edgecolor='black')
# 's' is used to set the size of the markers
# 'alpha' is used to set the transparency of the markers

# Adding labels and title
plt.xlabel('X-axis', fontsize=12, color='blue')
plt.ylabel('Y-axis', fontsize=12, color='blue')
plt.title('Scatter Plot Example', fontsize=14, fontweight='bold', color='purple')

# Adding grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()