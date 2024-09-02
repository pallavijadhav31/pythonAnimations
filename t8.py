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
image_path = "ice2.jpg"  # Provide the path to your image
try:
    image = pygame.image.load(image_path)
except pygame.error:
    print("Could not load image:", image_path)
    sys.exit()

# Set up colors
WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Iterate over each pixel in the image
    for y in range(image.get_height()):
        for x in range(image.get_width()):
            color = image.get_at((x, y))  # Get the color of the pixel
            if color != WHITE:  # Check if the color is not white
                rect = pygame.Rect(x, y, 1, 1)  # Create a rectangle for the pixel
                pygame.draw.rect(screen, color, rect)  # Draw the rectangle with the color

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
