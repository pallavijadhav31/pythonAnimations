import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the function to plot the heart shape
def plot_heart(x_offset, y_offset, scale):
    t = np.linspace(0, 2*np.pi, 100)
    x = scale * 16 * np.sin(t)**3 + x_offset
    y = scale * (13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)) + y_offset
    return x, y

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)

# Plot the initial heart shape
heart, = ax.plot([], [], 'r-')

# Define the initialization function
def init():
    heart.set_data([], [])
    return heart,

# Define the animation function
def animate(i):
    x, y = plot_heart(0, 0, 1 + 0.1*np.sin(i/10))
    heart.set_data(x, y)
    return heart,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=30, blit=True)

# Show the animation
plt.show()
