import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pendulum Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define pendulum parameters
pivot_x = screen_width // 2
pivot_y = 100
length = 200
angle = math.radians(90)  # Start angle (90 degrees, pointing downwards)
angular_velocity = 0.05  # Angular velocity (radians per frame)
gravity = 0.05  # Acceleration due to gravity

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Calculate the position of the pendulum bob
    bob_x = pivot_x + length * math.sin(angle)
    bob_y = pivot_y + length * math.cos(angle)

    # Draw the pendulum
    pygame.draw.line(screen, BLACK, (pivot_x, pivot_y), (bob_x, bob_y), 2)
    pygame.draw.circle(screen, BLACK, (int(bob_x), int(bob_y)), 10)

    # Update the angle (simple harmonic motion equation)
    angle += angular_velocity
    angular_velocity += gravity * math.sin(angle)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
