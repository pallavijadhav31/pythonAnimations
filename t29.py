import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Old Notebook")

# Define colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (169, 169, 169)

# Set the number of lines and line spacing
NUM_LINES = 30
LINE_SPACING = 20

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw horizontal lines
    for i in range(NUM_LINES):
        pygame.draw.line(screen, DARK_GRAY, (50, i * LINE_SPACING + 50), (SCREEN_WIDTH - 50, i * LINE_SPACING + 50))

    # Draw margin lines
    pygame.draw.line(screen, DARK_GRAY, (50, 0), (50, SCREEN_HEIGHT), 2)
    pygame.draw.line(screen, DARK_GRAY, (SCREEN_WIDTH - 50, 0), (SCREEN_WIDTH - 50, SCREEN_HEIGHT), 2)

    # Draw paper-like background
    pygame.draw.rect(screen, LIGHT_GRAY, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100))

    # Update the display
    pygame.display.update()
