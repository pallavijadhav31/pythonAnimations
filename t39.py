import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Generative Art")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Class for individual shapes
class Shape:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)

# Main loop
running = True
clock = pygame.time.Clock()

# List to store shapes drawn by the user
shapes = []

# Evolutionary loop
generation = 1
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Draw a shape at the mouse position when clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            size = random.randint(10, 50)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            shapes.append(Shape(mouse_x, mouse_y, size, color))

    # Clear the screen
    screen.fill(BLACK)

    # Draw shapes
    for shape in shapes:
        shape.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Print information about the current generation
    print(f"Generation {generation}, Number of Shapes: {len(shapes)}")
    generation += 1

# Quit Pygame
pygame.quit()
