import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Stars")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define Star class
class Star:
    def __init__(self):
        self.size = random.randint(2, 4)
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.speed_x = random.uniform(2, 4)
        self.speed_y = random.uniform(-1, 1)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# Create a list to hold the stars
stars = []

# Create initial stars
for _ in range(10):
    stars.append(Star())

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Move and draw each star
    for star in stars:
        star.move()
        star.draw()

        # Respawn star when it goes out of screen
        if star.x > screen_width:
            star.x = 0
            star.y = random.randint(0, screen_height)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
