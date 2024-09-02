import pygame
import sys
import math

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating Square Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Square properties
square_size = 100
square_center = (screen_width // 2, screen_height // 2)
rotation_speed = 2  # in degrees per frame

# Main game loop
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the vertices of the square
    vertices = []
    for i in range(4):
        x = square_center[0] + square_size * math.cos(math.radians(angle + i * 90))
        y = square_center[1] + square_size * math.sin(math.radians(angle + i * 90))
        vertices.append((x, y))

    # Draw the square
    pygame.draw.polygon(screen, RED, vertices)

    # Update angle for rotation
    angle += rotation_speed
    if angle >= 360:
        angle -= 360

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
