import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 600
height = 400

# Set up the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Glittery Ribbon')

# Define colors
WHITE = (255, 255, 255)
SPARKLE_COLORS = [(255, 215, 0), (127, 255, 212), (255, 105, 180), (65, 105, 225)]  # Yellow, Aqua, Pink, Royal Blue
RIBBON_COLOR = (255, 255, 255)  # White for the ribbon
BOX_COLOR = (50, 50, 50)  # Dark gray for the box

# Function to create a sparkle
def create_sparkle():
    return {
        'x': random.randint(width // 2 - 60, width // 2 + 60),
        'y': random.randint(height // 2 - 150, height // 2 - 50),
        'color': random.choice(SPARKLE_COLORS),
        'speed': random.randint(1, 3)
    }

# Create initial sparkles
sparkles = [create_sparkle() for _ in range(20)]

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill((0, 0, 0))

    # Draw the box
    pygame.draw.rect(window, BOX_COLOR, (width // 2 - 50, height // 2 - 50, 100, 100))

    # Draw the ribbon
    pygame.draw.polygon(window, RIBBON_COLOR, [(width // 2 - 60, height // 2 - 50),
                                               (width // 2 + 60, height // 2 - 50),
                                               (width // 2, height // 2 - 150)])

    # Update and draw sparkles
    for sparkle in sparkles:
        sparkle['y'] += sparkle['speed']
        if sparkle['y'] > height // 2 - 50:
            sparkle['y'] = random.randint(height // 2 - 150, height // 2 - 50)
            sparkle['x'] = random.randint(width // 2 - 60, width // 2 + 60)
            sparkle['speed'] = random.randint(1, 3)
        pygame.draw.circle(window, sparkle['color'], (sparkle['x'], sparkle['y']), 3)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
