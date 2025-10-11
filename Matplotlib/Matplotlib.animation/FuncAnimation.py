import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Moving the sine wave function using FuncAnimation
# FuncAnimation is used to create animations by repeatedly calling a function
# It takes the figure object, the function to call, the frames (number of times to call the function), and the interval (time between frames in milliseconds)

# Sample data
x = np.linspace(0, 2 * np.pi, 100) # value from 0 to 2π with 100 points
y = np.sin(x)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot(x, y, color='royalblue', linewidth=2.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Sine Wave Animation", fontsize=15, fontweight='bold', color='darkslategray')
ax.set_xlabel("X-axis → Angle (radians)", fontsize=12)
ax.set_ylabel("Y-axis → sin(x)", fontsize=12)
ax.grid(True, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)

# Update Function
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Update the y-data of the line
    return line

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50)
# saving the animation as a gif file
ani.save('sine_wave_animation.gif', writer='pillow') # Writer is used to specify the backend to use for saving the animation

plt.show()
