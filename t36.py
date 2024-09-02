import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Falling Objects Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
player_image = pygame.image.load("ice1.jpg").convert()
player_image.set_colorkey(BLACK)
player_rect = player_image.get_rect()

# Class for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = player_rect
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 20
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# Class for falling objects
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(random_color())
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)

# Function to generate random colors
def random_color():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# Set up sprite groups
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()

# Create player object
player = Player()
all_sprites.add(player)

# Main loop
running = True
clock = pygame.time.Clock()

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Spawn new objects
    if len(objects) < 10:
        obj = FallingObject()
        all_sprites.add(obj)
        objects.add(obj)

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, objects, True)

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
