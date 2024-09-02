import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Different Smileys")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Define Smiley class
class Smiley:
    def __init__(self, x, y, radius, eyes_radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.eyes_radius = eyes_radius

    def draw(self):
        # Draw face
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

        # Draw eyes
        left_eye_pos = (self.x - int(self.radius / 2), self.y - int(self.radius / 2))
        right_eye_pos = (self.x + int(self.radius / 2), self.y - int(self.radius / 2))
        pygame.draw.circle(screen, BLACK, left_eye_pos, self.eyes_radius)
        pygame.draw.circle(screen, BLACK, right_eye_pos, self.eyes_radius)

        # Draw mouth
        pygame.draw.arc(screen, BLACK, (self.x - int(self.radius / 2), self.y, self.radius, int(self.radius / 2)), 0, math.pi, 3)

# Create a list to hold the smiley objects
smileys = []

# Create initial smiley objects
for _ in range(5):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(20, 50)
    eyes_radius = random.randint(5, 10)
    smiley = Smiley(x, y, radius, eyes_radius)
    smileys.append(smiley)

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

    # Move and draw each smiley
    for smiley in smileys:
        smiley.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
