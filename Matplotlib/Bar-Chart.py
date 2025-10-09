import matplotlib.pyplot as plt

# bar charts in Matplotlib

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

# Create a bar chart
plt.bar(categories, values, color='skyblue', edgecolor='black')
# edgecolor is used to give border to the bars

# Adding labels and title
plt.xlabel('Categories', fontsize=12, color='blue')
plt.ylabel('Values', fontsize=12, color='blue')
plt.title('Bar Chart Example', fontsize=14, fontweight='bold', color='purple')

# Adding grid
plt.grid(axis='y', linestyle='--', linewidth=0.5)
# 'axis' can be 'x', 'y', or 'both'.
plt.ylim(0, 10) # Set y-axis limit
plt.savefig('bar_chart.png')  # Save the current figure as a PNG file
plt.show()