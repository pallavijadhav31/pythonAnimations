import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Bear")

# Colors
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
WHITE = (255, 255, 255)

# Define the bear class
class Bear:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load('Designer.png')

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

# Create the bear
bear = Bear(WIDTH // 2, HEIGHT // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Move the bear
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bear.move_left()
    if keys[pygame.K_RIGHT]:
        bear.move_right()

    # Draw the bear
    bear.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
