# import pygame
# import os

# # Initialize Pygame
# pygame.init()

# # Set the dimensions of the window
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Image Animation")

# # Load the image
# image_path = "birth.png"  # Replace "image.jpg" with the path to your image
# image = pygame.image.load(image_path)
# image_rect = image.get_rect()

# # Calculate the position to center the image
# image_rect.centerx = SCREEN_WIDTH // 2
# image_rect.centery = SCREEN_HEIGHT // 2

# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Clear the screen
#     screen.fill((255, 255, 255))

#     # Draw the image in the center of the screen
#     screen.blit(image, image_rect)

#     # Update the display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# --------------------------------------------------------------------------------

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
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
    particles.append(particle)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw particles
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

    # Draw the image in the center of the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
"""

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
image_path = "ice1.jpg"  # Replace "image.jpg" with the path to your image
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
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
    particles.append(particle)

# Define heart parameters
heart_image = pygame.image.load("birth.png")  # Replace "heart.png" with the path to your heart image
heart_rect = heart_image.get_rect()
heart_scale = 0.1  # Scale factor for the hearts

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw particles
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

    # Draw hearts
    for _ in range(num_particles // 4):  # Draw a quarter of the number of particles as hearts
        heart_x = random.randint(0, SCREEN_WIDTH - heart_rect.width)
        heart_y = random.randint(0, SCREEN_HEIGHT - heart_rect.height)
        screen.blit(pygame.transform.scale(heart_image, (int(heart_rect.width * heart_scale),
                                                         int(heart_rect.height * heart_scale))),
                    (heart_x, heart_y))

    # Draw the image in the center of the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
"""
