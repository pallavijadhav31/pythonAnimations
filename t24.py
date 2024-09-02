import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart and Dairy Milk Silk Animation")

# Define colors
RED = (255, 0, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Load images
heart_img = pygame.image.load('ice1.jpg')
silk_img = pygame.image.load('ice2.jpg')

# Scale images
heart_img = pygame.transform.scale(heart_img, (100, 100))
silk_img = pygame.transform.scale(silk_img, (100, 100))

# Initial positions
heart_x, heart_y = WIDTH // 4, HEIGHT // 2
silk_x, silk_y = 3 * WIDTH // 4, HEIGHT // 2

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move heart and silk
    heart_x += 1
    silk_x -= 1

    # Clear the screen
    screen.fill(BLACK)

    # Draw heart and silk
    screen.blit(heart_img, (heart_x, heart_y))
    screen.blit(silk_img, (silk_x, silk_y))

    # Draw the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
