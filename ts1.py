import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the notebook page
notebook_page = patches.Rectangle((0, 0), 6, 8, linewidth=2, edgecolor='black', facecolor='white')
ax.add_patch(notebook_page)

# Draw the lines on the notebook page
for i in range(1, 6):
    line = patches.Rectangle((0.5, i), 5, 0.05, linewidth=1, edgecolor='black', facecolor='lightgray')
    ax.add_patch(line)

# Add a cartoonish border around the page
border = patches.Rectangle((-0.1, -0.1), 6.2, 8.2, linewidth=3, edgecolor='black', facecolor='none')
ax.add_patch(border)

# Add some text
ax.text(0.5, 7.5, "My Notebook", fontsize=20, fontweight='bold')

# Set axis limits and hide axes
ax.set_xlim(0, 6)
ax.set_ylim(0, 8)
ax.axis('off')

# Show the cartoon-style notebook page
plt.show()
