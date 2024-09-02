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
image_path = "ice4.jpg"  # Provide the path to your image
try:
    image = pygame.image.load(image_path)
except pygame.error:
    print("Could not load image:", image_path)
    sys.exit()

# Set up the clock
clock = pygame.time.Clock()

# Function to perform flood fill
def flood_fill(x, y, target_color, replacement_color):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < image.get_width() and 0 <= y < image.get_height() and image.get_at((x, y)) == target_color:
            image.set_at((x, y), replacement_color)
            stack.extend([(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]])

# Perform flood fill to find connected components and draw black lines around them
for y in range(image.get_height()):
    for x in range(image.get_width()):
        color = image.get_at((x, y))
        if color != (255, 255, 255, 255):  # Ignore white color
            flood_fill(x, y, color, (255, 255, 255, 255))  # Fill connected component with white color

# Draw the black lines
for y in range(image.get_height()):
    for x in range(image.get_width()):
        if x + 1 < image.get_width() and image.get_at((x, y)) != image.get_at((x + 1, y)):
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 1, y))
        if y + 1 < image.get_height() and image.get_at((x, y)) != image.get_at((x, y + 1)):
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 1))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the image onto the screen
    screen.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
