import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Drawing")

# Load the image
image_path = "ice3.jpg"  # Provide the path to your image
try:
    image = pygame.image.load(image_path)
except pygame.error:
    print("Could not load image:", image_path)
    sys.exit()

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white color

    # Draw the image onto the screen
    screen.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
