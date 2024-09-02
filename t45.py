import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Star Field Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Class for representing a star
class Star:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.speed = random.randint(1, 5)

    def move(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = 0
            self.x = random.randint(0, screen_width)

# Create a list to hold the stars
stars = [Star() for _ in range(100)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, (star.x, star.y), 2)

    # Move the stars
    for star in stars:
        star.move()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
