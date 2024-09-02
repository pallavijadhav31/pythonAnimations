import pygame
import sys
import random
from PIL import Image, ImageOps
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ice Creams")

# Set up colors
WHITE = (255, 255, 255)

# Function to load and process ice cream image
def load_and_process_ice_cream_image(image_path):
    # Load image
    ice_cream_image = Image.open(image_path)
    ice_cream_image = ice_cream_image.convert("RGBA")

    # Convert image to NumPy array
    ice_cream_np = np.array(ice_cream_image)

    # Set transparent pixels to white
    ice_cream_np[(ice_cream_np[:, :, 3] == 0)] = [255, 255, 255, 0]

    # Convert back to PIL image
    ice_cream_image = Image.fromarray(ice_cream_np)

    # Invert image
    ice_cream_image = ImageOps.invert(ice_cream_image)

    # Convert to alpha mask
    alpha_mask = ice_cream_image.split()[3]

    # Create new blank image
    new_image = Image.new("RGBA", ice_cream_image.size, (255, 255, 255, 0))

    # Paste original image onto new image using alpha mask
    new_image.paste(ice_cream_image, (0, 0), alpha_mask)

    # Convert to pygame surface
    ice_cream_surface = pygame.image.fromstring(new_image.tobytes(), new_image.size, new_image.mode)

    return ice_cream_surface

# Load and process ice cream image
ice_cream_image_path = 'ice1.jpg'
# Define IceCream class
class IceCream:
    def __init__(self, image):
        self.image = image
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
    ice_creams.append(IceCream(ice_cream_surface))

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
