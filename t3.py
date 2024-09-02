import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Magic Balls")

# Set up colors
WHITE = (255, 255, 255)

# Define Ball class
class Ball:
    def __init__(self):
        self.radius = random.randint(10, 30)
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off the walls
        if self.x <= self.radius or self.x >= screen_width - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius or self.y >= screen_height - self.radius:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create a list to hold the balls
balls = []

# Create initial balls
for _ in range(10):
    balls.append(Ball())

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

    # Move and draw each ball
    for ball in balls:
        ball.move()
        ball.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
