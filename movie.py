import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters
duration = 10  # Duration of the animation in seconds
fps = 30  # Frames per second

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Function to update the animation
def update(frame):
    ax.clear()
    theta = np.linspace(0, 2*np.pi, 100)
    colors = plt.cm.viridis(np.linspace(0, 1, 10))
    for i, color in enumerate(colors):
        x = np.cos(theta + i*frame/50)
        y = np.sin(theta + i*frame/50)
        ax.plot(x, y, color=color, lw=2)
    ax.set_title('Mesmerizing Pattern')
    ax.axis('off')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, duration * fps), interval=1000 / fps)

# Save the animation as a video file
ani.save('mesmerizing_pattern.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

# Show the animation
plt.show()
