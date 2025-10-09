import matplotlib.pyplot as plt

# Pyplot is a collection of functions that make Matplotlib work like MATLAB. Each pyplot function makes some change to a figure:
# e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.


# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a simple line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Display the plot
plt.show()

# To Save the plot as an image file
plt.savefig('simple_line_plot.png')  # Save the current figure as a PNG file