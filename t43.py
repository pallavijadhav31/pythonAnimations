import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Writing Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the text and font
text = "Hello, World! I'm Pallavi"
font = pygame.font.SysFont(None, 48)
text_surface = font.render(text, True, BLACK)
text_width, text_height = text_surface.get_size()

# Animation parameters
animation_speed = 50  # Number of milliseconds between each letter appearing
current_index = 0

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Get the portion of the text to display
    displayed_text = text[:current_index]
    displayed_surface = font.render(displayed_text, True, BLACK)

    # Blit the displayed text onto the screen
    screen.blit(displayed_surface, ((screen_width - text_width) // 2, (screen_height - text_height) // 2))

    # Update the display
    pygame.display.flip()

    # Increment the index to reveal the next letter
    if current_index < len(text):
        current_index += 1

    # Cap the frame rate
    clock.tick(60)

    # Pause to control the animation speed
    pygame.time.delay(animation_speed)

# Quit Pygame
pygame.quit()
