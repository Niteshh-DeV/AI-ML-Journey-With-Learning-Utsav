"""
Topics Covered:
1. Object-Oriented Interface (Figure & Axes)
2. Titles, Labels, Legends
3. Ticks & Spines
4. Annotations
5. Custom Styles & Grid Customization
"""

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100) # value from 0 to 10 with 100 points
y1 = np.sin(x)
y2 = np.cos(x)

# Create figure and axes using Object-Oriented Interface
fig, ax = plt.subplots(figsize=(8, 5))

# Plot multiple lines
ax.plot(x, y1, label='sin(x)', color='royalblue', linewidth=2.5, linestyle='-')
ax.plot(x, y2, label='cos(x)', color='orange', linewidth=2, linestyle='--')

# ------------------------------
#  Titles and Labels
# ------------------------------
ax.set_title("Advanced Matplotlib Customization", fontsize=15, fontweight='bold', color='darkslategray')
ax.set_xlabel("X-axis → Angle (radians)", fontsize=12)
ax.set_ylabel("Y-axis → Function Value", fontsize=12)

# ------------------------------
#  Grid Customization
# ------------------------------
ax.grid(True, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)

# ------------------------------
#  Legend Customization
# ------------------------------
ax.legend(loc='best', fontsize=10, frameon=True, shadow=True)

# ------------------------------
#  Ticks Customization
# Ticks are the markers denoting data points on axes
# ------------------------------
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(-1, 1.1, 0.5))
ax.tick_params(axis='both', direction='inout', length=6, colors='purple')

# ------------------------------
#  Spines Customization
#  Spines are the lines connecting the axis tick marks and noting the boundaries of the data area
# ------------------------------
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('gray')
ax.spines['bottom'].set_color('gray')

# ------------------------------
#  Annotation
# ------------------------------
ax.annotate(
    'Peak Point',
    xy=(np.pi/2, 1),
    xytext=(2, 1.2),
    arrowprops=dict(facecolor='green', shrink=0.05, width=1.5),
    fontsize=10,
    color='green'
)

# ------------------------------
#  Style Customization
#  Styles are pre-defined themes for Matplotlib plots
# ------------------------------
plt.style.use('seaborn-v0_8-darkgrid')  # (You can try 'ggplot', 'bmh', 'fivethirtyeight')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("day14_matplotlib_advanced.png", dpi=300)

# Show the figure
plt.show()