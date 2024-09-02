import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Greeting Card")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Background animation variables
background_color = BLACK
background_animation_speed = 0.05
background_max_intensity = 255
background_min_intensity = 50
background_current_intensity = background_max_intensity
background_increasing_intensity = False

# Greeting card animation variables
card_color = WHITE
card_animation_speed = 0.1
card_max_alpha = 255
card_min_alpha = 100
card_current_alpha = card_max_alpha
card_increasing_alpha = False

# Font initialization
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

# Message text
message = ""

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle clicking on the greeting card
            if pygame.Rect(100, 400, 600, 100).collidepoint(event.pos):
                # Change card color on click
                if event.button == 1:  # Left mouse button
                    card_color = RED if card_color != RED else GREEN
                # Handle typing messages
                elif event.button == 3:  # Right mouse button
                    if pygame.Rect(100, 400, 600, 100).collidepoint(pygame.mouse.get_pos()):
                        if event.key == pygame.K_BACKSPACE:
                            message = message[:-1]
                        else:
                            message += event.unicode

    # Update background color animation
    if background_increasing_intensity:
        background_current_intensity += background_animation_speed
        if background_current_intensity >= background_max_intensity:
            background_increasing_intensity = False
    else:
        background_current_intensity -= background_animation_speed
        if background_current_intensity <= background_min_intensity:
            background_increasing_intensity = True

    # Update greeting card animation
    if card_increasing_alpha:
        card_current_alpha += card_animation_speed
        if card_current_alpha >= card_max_alpha:
            card_increasing_alpha = False
    else:
        card_current_alpha -= card_animation_speed
        if card_current_alpha <= card_min_alpha:
            card_increasing_alpha = True

    # Clear the screen
    # screen.fill((background_color, background_current_intensity))
    # Combine background color and intensity into a single RGB tuple
    background_color_with_intensity = (background_color, int(background_current_intensity))

# Clear the screen
    screen.fill(background_color_with_intensity)

    # Draw the greeting card
    pygame.draw.rect(screen, card_color + (int(card_current_alpha),), (100, 400, 600, 100))
    pygame.draw.rect(screen, BLACK, (100, 400, 600, 100), 2)

    # Render and display the message
    text_surface = font.render(message, True, BLACK)
    screen.blit(text_surface, (110, 410))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
