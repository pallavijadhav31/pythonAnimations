import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ice Cream Cones")

# Set up colors
WHITE = (255, 255, 255)

# Load ice cream images
ice_cream_images = [
    pygame.image.load("ice1.jpg").convert_alpha(),
    pygame.image.load("ice2.jpg").convert_alpha(),
    pygame.image.load("ice3.jpg").convert_alpha()
]

# Define IceCream class
class IceCream:
    def __init__(self):
        self.image = random.choice(ice_cream_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y *= -1

    def draw(self):
        screen.blit(self.image, self.rect)

# Create a list to hold the ice cream cones
ice_creams = []

# Create initial ice cream cones
for _ in range(5):
    ice_creams.append(IceCream())

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

    # Move and draw each ice cream cone
    for ice_cream in ice_creams:
        ice_cream.move()
        ice_cream.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
