import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the ball properties
ball_radius = 20
ball_color = RED
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = [5, 5]  # Initial velocity of the ball

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls
    if ball_pos[0] + ball_radius > screen_width or ball_pos[0] - ball_radius < 0:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] + ball_radius > screen_height or ball_pos[1] - ball_radius < 0:
        ball_speed[1] = -ball_speed[1]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
