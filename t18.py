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

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    window.fill((0, 0, 0))

    # Randomly move and draw the text with colorful effects
    for _ in range(10):
        x_offset = random.randint(-5, 5)
        y_offset = random.randint(-5, 5)
        color = random.choice(COLORS)
        rotated_text = pygame.transform.rotate(text, random.randint(-30, 30))
        window.blit(rotated_text, (width // 2 - rotated_text.get_width() // 2 + x_offset,
                                   height // 2 - rotated_text.get_height() // 2 + y_offset))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)

# Quit pygame
pygame.quit()
