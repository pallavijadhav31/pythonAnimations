import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 600
height = 400

# Set up the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Glittery Box')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill(BLACK)

    # Create a glittery effect by drawing random white dots
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        pygame.draw.circle(window, WHITE, (x, y), 2)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
