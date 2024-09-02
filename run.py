import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Running Smiley")

# Load images
smiley_img = pygame.image.load("bear.png")

# Get the width and height of the smiley image
smiley_width, smiley_height = smiley_img.get_width(), smiley_img.get_height()

# Set up variables for smiley's position and movement
x, y = 0, height - smiley_height
speed = 5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the smiley
    x += speed
    if x > width:
        x = -smiley_width

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the smiley
    screen.blit(smiley_img, (x, y))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(30)
