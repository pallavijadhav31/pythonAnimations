import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Falling Leaves")

# Set up colors
WHITE = (255, 255, 255)

# Define Leaf class
class Leaf:
    def __init__(self):
        self.size = random.randint(10, 20)
        self.x = random.randint(0, screen_width)
        self.y = -self.size
        self.speed_y = random.randint(1, 5)
        self.color = (random.randint(100, 150), random.randint(200, 255), random.randint(100, 150))

    def move(self):
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.size)

# Create a list to hold the leaves
leaves = []

# Create initial leaves
for _ in range(50):
    leaves.append(Leaf())

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

    # Move and draw each leaf
    for leaf in leaves:
        leaf.move()
        leaf.draw()

        # Reset leaf position if it reaches the bottom of the screen
        if leaf.y > screen_height + leaf.size:
            leaf.y = -leaf.size
            leaf.x = random.randint(0, screen_width)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
