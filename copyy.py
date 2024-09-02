import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cartoon Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define constants for animation
x_pos = 50
y_pos = 300
velocity = 5

# Main animation loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw shapes (cartoon characters)
    pygame.draw.circle(screen, BLUE, (x_pos, y_pos), 30)  # Head
    pygame.draw.rect(screen, RED, (x_pos - 20, y_pos + 30, 40, 60))  # Body
    pygame.draw.line(screen, BLACK, (x_pos, y_pos + 30), (x_pos - 20, y_pos + 90), 3)  # Left leg
    pygame.draw.line(screen, BLACK, (x_pos, y_pos + 30), (x_pos + 20, y_pos + 90), 3)  # Right leg
    pygame.draw.line(screen, BLACK, (x_pos, y_pos), (x_pos - 10, y_pos - 10), 3)  # Left eye
    pygame.draw.line(screen, BLACK, (x_pos, y_pos), (x_pos + 10, y_pos - 10), 3)  # Right eye
    pygame.draw.arc(screen, BLACK, (x_pos - 15, y_pos - 15, 30, 20), 0, -3.14, 3)  # Mouth

    # Update character position
    x_pos += velocity
    if x_pos > width + 50:
        x_pos = -50

    # Update the display
    pygame.display.flip()

    # Delay to control animation speed
    time.sleep(0.05)

# Quit Pygame
pygame.quit()
