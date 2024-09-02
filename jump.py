import pygame
import sys

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping and Walking Image")

# Load the image
image = pygame.image.load("download.jpg")
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

# Variables for animation
jumping = False
jump_count = 10
walk_count = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True

    # Jumping animation
    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            image_rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Walking animation
    if keys[pygame.K_RIGHT]:
        walk_count += 1
        image_rect.x += 5

    # Drawing
    screen.fill((255, 255, 255))
    screen.blit(image, image_rect)
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
