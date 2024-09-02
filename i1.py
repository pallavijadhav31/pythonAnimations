import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ice Creams")

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
    def __init__(self, image):
        self.image = pygame.transform.scale(image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -20)   # Set y-coordinate for top row
        self.speed_x = random.randint(1, 3)

    def move(self):
        self.rect.y += self.speed_x

        if self.rect.y < 20 or self.rect.y > 50:
            self.speed_x *= -1
        # Bounce off the walls
        # if self.rect.left < 0 or self.rect.right > screen_width:
        #     self.speed_x *= -1

    def draw(self):
        screen.blit(self.image, self.rect)

# Create a list to hold the ice cream cones in the header
header_ice_creams = []

# Create ice cream cones in the header
for _ in range(3):
    ice_cream = IceCream(random.choice(ice_cream_images))
    ice_cream.rect.y = random.randint(-50, -20)  # Random initial y-coordinate above the screen
    ice_cream.rect.x = random.randint(0, screen_width - ice_cream.rect.width)  # Random x-coordinate
    header_ice_creams.append(ice_cream)

    # ice_cream = IceCream(random.choice(ice_cream_images))
    # ice_cream.rect.y = random.randint(20, 50)  # Random y-coordinate within the header area
    # header_ice_creams.append(ice_cream)


    # ice_cream = IceCream(random.choice(ice_cream_images))
    # header_ice_creams.append(ice_cream)

# Set up the font
font = pygame.font.SysFont(None, 48)

# Render the text
text_surface = font.render("Happy Birthday", True, WHITE)
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))

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

    # Move and draw each ice cream cone in the header
    for ice_cream in header_ice_creams:
        ice_cream.move()
        ice_cream.draw()

    # Draw the text in the center
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
