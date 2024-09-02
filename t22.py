import pygame
import math
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 800
height = 600

# Set up the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Glowing Flower')

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Function to draw a flower with a glowing effect
def draw_flower(surface, x, y, size, glow_opacity):
    # Draw flower petals with glowing effect
    for angle in range(0, 360, 45):
        x_end = x + size * math.cos(math.radians(angle))
        y_end = y + size * math.sin(math.radians(angle))
        pygame.draw.line(surface, (0, 255, 0, glow_opacity), (x, y), (x_end, y_end), size // 10)

    # Draw flower center
    pygame.draw.circle(surface, BLACK, (x, y), size // 4)

# Main loop
running = True
glow_opacity = 0  # Initial opacity for glowing effect

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill(BLACK)

    # Increase glow opacity gradually
    glow_opacity += 5
    if glow_opacity > 255:
        glow_opacity = 255

    # Draw the flower with glowing effect
    x = width // 2
    y = height // 2
    size = 200
    draw_flower(window, x, y, size, glow_opacity)

    # Gradually add color to the flower
    pygame.draw.circle(window, GREEN, (x, y), size // 4)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
