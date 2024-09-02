import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fireworks Display")

# Load background image
background_image = pygame.image.load("hb.gif").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)

# Function to generate random sparkling colors with slight variation
def random_color():
    base_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    color_variation = random.randint(-50, 50)
    return tuple(max(0, min(255, c + color_variation)) for c in base_color)

# Function to create a firework explosion
def create_explosion(x, y):
    num_particles = 100
    particles = []
    for _ in range(num_particles):
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        color = random_color()
        particles.append([x, y, dx, dy, color])

    return particles

# Main loop
running = True
clock = pygame.time.Clock()
fireworks = []

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create a firework explosion at the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            fireworks.extend(create_explosion(mouse_x, mouse_y))

    # Draw background image
    screen.blit(background_image, (0, 0))

    # Update and draw fireworks
    for firework in fireworks:
        firework[0] += firework[2]  # Update x position
        firework[1] += firework[3]  # Update y position
        pygame.draw.circle(screen, firework[4], (int(firework[0]), int(firework[1])), 3)  # Draw particle
        firework[3] += 0.05  # Add gravity effect
        if firework[1] >= screen_height:  # If particle is out of screen, remove it
            fireworks.remove(firework)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
