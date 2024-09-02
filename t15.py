import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 600
height = 400

# Set up the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Glittery Animation')

# Define colors
WHITE = (255, 255, 255)
COLORS = [(255, 215, 0), (127, 255, 212), (255, 105, 180), (65, 105, 225)]  # Yellow, Aqua, Pink, Royal Blue

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill((0, 0, 0))

    # Draw glittery lines
    for _ in range(10):
        x_start = random.randint(0, width)
        y_start = random.randint(0, height)
        x_end = random.randint(0, width)
        y_end = random.randint(0, height)
        color = random.choice(COLORS)
        pygame.draw.line(window, color, (x_start, y_start), (x_end, y_end), random.randint(1, 3))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
