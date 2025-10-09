import matplotlib.pyplot as plt

# Multiline plots in Matplotlib

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

# Create a multiline plot
plt.plot(x, y1, label='Increasing', color='blue', marker='o')
plt.plot(x, y2, label='Decreasing', color='red', marker='s')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiline Plot Example')

# Adding legend
plt.legend(loc = 'best')

# Adding Grid
plt.grid(True)

plt.show()