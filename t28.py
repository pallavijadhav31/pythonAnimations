import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Animation")

# Load the image
image_path = "birth.png"  # Replace "image.jpg" with the path to your image
image = pygame.image.load(image_path)
image_rect = image.get_rect()

# Calculate the position to center the image
image_rect.centerx = SCREEN_WIDTH // 2
image_rect.centery = SCREEN_HEIGHT // 2

# Define particle parameters
num_particles = 100
particles = []
for _ in range(num_particles):
    particle = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(1, 3),
                (random.randint(200, 255), random.randint(200, 255), random.randint(0, 255))]
    particles.append(particle)

# Define flower parameters
flower_image = pygame.image.load("birth.png")  # Replace "flower.png" with the path to your flower image
flower_rect = flower_image.get_rect()
flower_scale = 0.1  # Scale factor for the flowers

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw particles (celebration sparkles)
    for particle in particles:
        pygame.draw.circle(screen, particle[3], particle[:2], particle[2])

        # Update particle position (simple movement)
        particle[0] += random.randint(-2, 2)
        particle[1] += random.randint(-2, 2)

        # Check boundaries
        if particle[0] < 0:
            particle[0] = SCREEN_WIDTH
        elif particle[0] > SCREEN_WIDTH:
            particle[0] = 0

        if particle[1] < 0:
            particle[1] = SCREEN_HEIGHT
        elif particle[1] > SCREEN_HEIGHT:
            particle[1] = 0

    # Draw flowers
    for _ in range(num_particles // 4):  # Draw a quarter of the number of particles as flowers
        flower_x = random.randint(0, SCREEN_WIDTH - flower_rect.width)
        flower_y = random.randint(0, SCREEN_HEIGHT - flower_rect.height)
        screen.blit(pygame.transform.scale(flower_image, (int(flower_rect.width * flower_scale),
                                                          int(flower_rect.height * flower_scale))),
                    (flower_x, flower_y))

    # Draw the image in the center of the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
