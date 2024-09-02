import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 800
height = 600

# Set up the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Birthday Card')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Define font
font = pygame.font.Font(None, 50)

# Create a surface for the background
background = pygame.Surface((width, height))
background.fill(WHITE)

# Draw balloons
def draw_balloons(surface):
    for _ in range(10):
        x = random.randint(0, width)
        y = random.randint(height // 2, height)
        pygame.draw.circle(surface, random.choice([RED, BLUE, GREEN, YELLOW]), (x, y), random.randint(10, 30))

# Draw gifts
def draw_gifts(surface):
    for _ in range(5):
        x = random.randint(0, width)
        y = random.randint(height // 2, height)
        pygame.draw.rect(surface, random.choice([RED, BLUE, GREEN, YELLOW]), (x, y, 30, 30))

# Draw ice creams
def draw_ice_creams(surface):
    for _ in range(5):
        x = random.randint(0, width)
        y = random.randint(height // 2, height)
        pygame.draw.polygon(surface, random.choice([RED, BLUE, GREEN, YELLOW]),
                            [(x, y), (x + 20, y - 50), (x + 40, y), (x, y)])

# Draw cake with candles
def draw_cake(surface):
    x = width // 2 - 100
    y = height // 2 + 50
    pygame.draw.rect(surface, YELLOW, (x, y, 200, 150))
    pygame.draw.line(surface, BLACK, (x + 50, y), (x + 50, y - 50), 3)
    pygame.draw.line(surface, BLACK, (x + 100, y), (x + 100, y - 50), 3)
    pygame.draw.line(surface, BLACK, (x + 150, y), (x + 150, y - 50), 3)

# Draw text
def draw_text(surface):
    text = font.render('Happy Birthday!', True, BLACK)
    surface.blit(text, (width // 2 - text.get_width() // 2, 50))

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with white background
    window.blit(background, (0, 0))

    # Draw balloons, gifts, ice creams, cake, and text
    draw_balloons(window)
    draw_gifts(window)
    draw_ice_creams(window)
    draw_cake(window)
    draw_text(window)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
