import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (128, 0, 128)]

# Function to draw a circle at mouse position with random color
def draw_circle(pos):
    color = random.choice(COLORS)
    radius = random.randint(10, 50)
    pygame.draw.circle(screen, color, pos, radius)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                draw_circle(event.pos)

    # Update display
    pygame.display.flip()
    screen.fill(BLACK)  # Clear screen

# Quit Pygame
pygame.quit()
sys.exit()
