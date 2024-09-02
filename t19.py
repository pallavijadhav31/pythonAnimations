import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 800
height = 600

# Set up the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hurray Animation')

# Define colors
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow

# Define font
font = pygame.font.Font(None, 100)

# Define the text
text = font.render('Hurray!', True, WHITE)

# Balloon class
class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 30))
        self.image.fill(random.choice(COLORS))
        pygame.draw.ellipse(self.image, WHITE, [0, 0, 20, 30], 2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = height

    def update(self):
        self.rect.y -= random.randint(1, 3)
        if self.rect.y < -30:
            self.rect.y = height
            self.rect.x = random.randrange(width)

# Create sprite group for balloons
all_sprites = pygame.sprite.Group()
for _ in range(20):
    balloon = Balloon()
    all_sprites.add(balloon)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill((0, 0, 0))

    # Update and draw balloons
    all_sprites.update()
    all_sprites.draw(window)

    # Randomly move and draw the text
    x_offset = random.randint(-5, 5)
    y_offset = random.randint(-5, 5)
    color = random.choice(COLORS)
    rotated_text = pygame.transform.rotate(text, random.randint(-5, 5))
    window.blit(rotated_text, (width // 2 - rotated_text.get_width() // 2 + x_offset,
                               height // 2 - rotated_text.get_height() // 2 + y_offset))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
