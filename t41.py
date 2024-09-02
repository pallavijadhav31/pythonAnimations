import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Simulation")

# Define colors
WHITE = (255, 255, 255)

# Class for representing a bouncing ball
class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def check_collision(self):
        # Check collision with walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.dx *= -1
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.dy *= -1
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Main loop
running = True
clock = pygame.time.Clock()

# Create a bouncing ball
ball = Ball(screen_width // 2, screen_height // 2, 20, (255, 0, 0), 5)

# Simulation loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball.move()

    # Check collision
    ball.check_collision()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    ball.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
