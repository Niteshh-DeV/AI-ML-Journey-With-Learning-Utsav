import matplotlib.pyplot as plt
import numpy as np

# Pie chart data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode the 1st slice
# 'explode' is used to offset a slice from the center of the pie

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
#Startangle is used to rotate the start of the pie chart

plt.title('Pie Chart Example', fontsize=14, fontweight='bold', color='purple')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()