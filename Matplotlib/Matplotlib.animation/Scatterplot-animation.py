import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

fig, ax = plt.subplots()
scat = ax.scatter(x, y, color='crimson')

def update(frame):
    y = np.sin(x + frame / 10)
    scat.set_offsets(np.c_[x, y])
    return scat,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.title("Animated Scatter Plot")
plt.show()