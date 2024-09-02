import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Animation")

# Define colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define the heart shape points
heart_shape = [
    (400, 300),
    (400, 200),
    (300, 100),
    (200, 200),
    (200, 300),
]

# Define animation parameters
animation_speed = 1
direction = 'down'

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw heart shape
    pygame.draw.polygon(screen, RED, heart_shape)

    # Animate the heart shape
    if direction == 'down':
        heart_shape[0] = (heart_shape[0][0], heart_shape[0][1] + animation_speed)
        heart_shape[1] = (heart_shape[1][0], heart_shape[1][1] + animation_speed)
        heart_shape[3] = (heart_shape[3][0], heart_shape[3][1] + animation_speed)
        heart_shape[4] = (heart_shape[4][0], heart_shape[4][1] + animation_speed)
        if heart_shape[0][1] >= HEIGHT:
            direction = 'up'
    elif direction == 'up':
        heart_shape[0] = (heart_shape[0][0], heart_shape[0][1] - animation_speed)
        heart_shape[1] = (heart_shape[1][0], heart_shape[1][1] - animation_speed)
        heart_shape[3] = (heart_shape[3][0], heart_shape[3][1] - animation_speed)
        heart_shape[4] = (heart_shape[4][0], heart_shape[4][1] - animation_speed)
        if heart_shape[0][1] <= 0:
            direction = 'down'

    # Draw the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
