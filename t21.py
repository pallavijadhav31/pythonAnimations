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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Function to draw a flower
def draw_flower(surface, x, y, size):
    # Draw petals
    for angle in range(0, 360, 45):
        x_pos = x + size * math.cos(math.radians(angle))
        y_pos = y + size * math.sin(math.radians(angle))
        pygame.draw.circle(surface, YELLOW, (int(x_pos), int(y_pos)), size // 2)

    # Draw flower center
    pygame.draw.circle(surface, BLACK, (x, y), size // 4)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill(BLACK)

    # Draw a glowing flower
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    size = random.randint(20, 50)
    draw_flower(window, x, y, size)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)

# Quit pygame
pygame.quit()
