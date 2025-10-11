import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

# Data
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("ArtistAnimation — Sine Wave")

# Pre-create frames
frames = []
for phase in np.linspace(0, 2*np.pi, 60):
    line, = ax.plot(x, np.sin(x + phase), color='royalblue')
    frames.append([line])  # Each frame is a list of artists

# Create animation
ani = ArtistAnimation(fig, frames, interval=50, blit=True) # blit=True for optimized drawing

plt.show()