import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sparkling Animation")

# Load background image
background_image = pygame.image.load("ice1.jpg").convert()

# Define colors
WHITE = (255, 255, 255)

# Function to generate random sparkling colors with slight variation
def random_color():
    base_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color_variation = random.randint(-50, 50)
    return tuple(max(0, min(255, c + color_variation)) for c in base_color)

# Main loop
running = True
clock = pygame.time.Clock()
sparkles = []

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a new sparkle where the mouse was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            sparkles.append([mouse_x, mouse_y, random.randint(1, 5), random_color(), random.randint(2, 6)])

    # Draw background image
    screen.blit(background_image, (0, 0))
    
    # Draw and update sparkles
    for sparkle in sparkles:
        sparkle[1] += sparkle[2]  # Move sparkle downwards
        pygame.draw.circle(screen, sparkle[3], (sparkle[0], sparkle[1]), sparkle[4])  # Draw sparkle
        if sparkle[1] > screen_height + 20:  # If sparkle is out of screen, remove it
            sparkles.remove(sparkle)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
