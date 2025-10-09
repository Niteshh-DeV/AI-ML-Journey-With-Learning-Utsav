import matplotlib.pyplot as plt

# Customizing Plots in Matplotlib

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a simple line plot with customizations
plt.plot(x, y, color='blue', linestyle='--', marker='o', markersize=4, label='Line 1')
# here marker is used to show the data points

plt.plot(x, [i**1.5 for i in y], color='red', linestyle='-', marker='s', markersize=6, label='Line 2')
# Here i**1.5 is used to show the exponential growth

# Adding labels and title with custom font sizes
plt.xlabel('X-axis', fontsize=14, color='green')
plt.ylabel('Y-axis', fontsize=14, color='gray')
plt.title('Customized Line Plot', fontsize=16, fontweight='bold', color='purple')

# Adding grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# 'which' can be 'major', 'minor', or 'both'.

# Adding legend
# Legenrd is used to show the label of the lines
plt.legend(loc='upper left', fontsize=10)
# 'loc' can be 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center etc.

# Customizing axes limits
plt.xlim(0, 6) # 0,6 is the range of x-axis
plt.ylim(0, 40) # 0,40 is the range of y-axis

# Display the plot
plt.show()
plt.savefig('customized_line_plot.png')  # Save the current figure as a PNG file