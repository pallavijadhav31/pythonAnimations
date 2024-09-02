import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cartoon Animation")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw a simple cartoon character (a blue circle for the head)
    pygame.draw.circle(screen, BLUE, (screen_width // 2, screen_height // 2), 50)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
sys.exit()
