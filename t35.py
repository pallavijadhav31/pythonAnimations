import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Particle System")

# Define colors
WHITE = (255, 255, 255)

# Function to generate random colors
def random_color():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# Class for individual particles
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(5, 10)
        self.color = random_color()
        self.speed = random.uniform(0.1, 0.5)
        self.angle = random.uniform(0, 2 * 3.14159)

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = max(1, ((dx ** 2) + (dy ** 2)) ** 0.5)
        self.x += dx * self.speed / distance
        self.y += dy * self.speed / distance

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Main loop
running = True
clock = pygame.time.Clock()
particles = []

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move particles towards the mouse cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for particle in particles:
        particle.move_towards(mouse_x, mouse_y)

    # Create new particles when mouse button is pressed
    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        particles.append(Particle(mouse_x, mouse_y))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw and update particles
    for particle in particles:
        particle.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
