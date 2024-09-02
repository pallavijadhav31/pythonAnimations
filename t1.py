import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

# Set the axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

# Initialization function
def init():
    ln.set_data([], [])
    return ln,

# Animation function
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100),
                    init_func=init, blit=True)

plt.show()
