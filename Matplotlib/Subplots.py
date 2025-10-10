import matplotlib.pyplot as plt
import numpy as np

# Subplots allows to create multiple plots in a single figure.

# Sample data
x = np.linspace(0, 10, 100)
# linspace is used to create an array of evenly spaced values over a specified range

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y3 = np.clip(y3, -10, 10)  # Clipping to avoid extreme values in tan plot
# .clip is used to limit the values in an array, here we limit the values of y3 between -10 and 10

# Create subplots
fig , axs = plt.subplots(2, 2, figsize=(10, 10))
# 2 rows, 2 column
fig.suptitle('Multiple Subplots Example', fontsize=16, fontweight='bold', color='purple')
fig.tight_layout(pad=3.0)
# tight_layout is used to automatically adjust subplot parameters to give specified padding

# First subplot
axs[0, 0].plot(x, y1, color='blue', label='sin(x)')
axs[0, 0].set_title('Sine Function', fontsize=12, color='blue')
axs[0, 0].set_xlabel('X-axis', fontsize=10)
axs[0, 0].set_ylabel('sin(x)', fontsize=10)
axs[0, 0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[0, 0].legend()

# Second subplot
axs[0, 1].plot(x, y2, color='red', label='cos(x)')
axs[0, 1].set_title('Cosine Function', fontsize=12, color='red')
axs[0, 1].set_xlabel('X-axis', fontsize=10)
axs[0, 1].set_ylabel('cos(x)', fontsize=10)
axs[0, 1].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[0, 1].legend()

# Third subplot
axs[1, 0].plot(x, y3, color='green', label='tan(x)')
axs[1, 0].set_title('Tangent Function', fontsize=12, color='green')
axs[1, 0].set_xlabel('X-axis', fontsize=10)
axs[1, 0].set_ylabel('tan(x)', fontsize=10)
axs[1, 0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[1, 0].legend()

# Fourth sublopt
axs[1,1].pie([15, 30, 45, 10], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
axs[1,1].set_title('Pie Chart', fontsize=12, color='purple')

plt.tight_layout()
# Adjust layout to prevent overlap
plt.show()