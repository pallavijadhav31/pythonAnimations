import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("House and Clouds Animation")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Set up the house
house_width = 200
house_height = 300
house_x = screen_width // 2 - house_width // 2
house_y = screen_height - house_height
roof_points = [(house_x, house_y), (house_x + house_width // 2, house_y - 150), (house_x + house_width, house_y)]
door_width = 60
door_height = 120
door_x = house_x + house_width // 2 - door_width // 2
door_y = house_y + house_height - door_height
window_width = 50
window_height = 50
window_x = house_x + house_width // 4
window_y = house_y + house_height // 4
window_padding = 20

# Set up the clouds
clouds = []
for _ in range(3):
    cloud_x = random.randint(-200, screen_width)
    cloud_y = random.randint(50, 200)
    cloud_speed = random.randint(1, 3)
    clouds.append((cloud_x, cloud_y, cloud_speed))

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLUE)

    # Draw the house
    pygame.draw.polygon(screen, GRAY, roof_points)
    pygame.draw.rect(screen, YELLOW, (house_x, house_y, house_width, house_height))
    pygame.draw.rect(screen, GRAY, (door_x, door_y, door_width, door_height))
    pygame.draw.rect(screen, GRAY, (window_x, window_y, window_width, window_height))
    pygame.draw.rect(screen, GRAY, (window_x + 2 * window_padding + window_width, window_y, window_width, window_height))

    # Draw and move the clouds
    for i in range(len(clouds)):
        cloud_x, cloud_y, cloud_speed = clouds[i]
        pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), 40)
        cloud_x += cloud_speed
        if cloud_x > screen_width:
            cloud_x = -200
            cloud_y = random.randint(50, 200)
        clouds[i] = (cloud_x, cloud_y, cloud_speed)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
