import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cute Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Define the smiley face
class Smiley:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = 5  # Velocity in x direction
        self.dy = 5  # Velocity in y direction

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, BLACK, (self.x - self.radius//2, self.y - self.radius//4), self.radius//10)
        pygame.draw.circle(screen, BLACK, (self.x + self.radius//2, self.y - self.radius//4), self.radius//10)
        pygame.draw.arc(screen, BLACK, (self.x - self.radius//2, self.y, self.radius, self.radius//2), 
                        0, 3.14, 3)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the edges of the screen
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.dy = -self.dy

# Create the smiley face
smiley = Smiley(WIDTH // 2, HEIGHT // 2, 50, YELLOW)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Update and draw the smiley face
    smiley.update()
    smiley.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
