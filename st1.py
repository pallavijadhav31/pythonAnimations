import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Twinkling Stars")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define Star class
class Star:
    def __init__(self):
        self.size = random.randint(1, 3)
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.alpha = random.randint(100, 255)  # Transparency level
        self.color = (self.alpha, self.alpha, self.alpha)

    def twinkling(self):
        # Randomly change transparency to simulate twinkling
        self.alpha += random.randint(-10, 10)
        self.alpha = max(50, min(255, self.alpha))  # Clamp transparency within range
        self.color = (self.alpha, self.alpha, self.alpha)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Create a list to hold the stars
stars = []

# Create initial stars
for _ in range(100):
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

    # Twinkle and draw each star
    for star in stars:
        star.twinkling()
        star.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()
