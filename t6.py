import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Letter Cartoon")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define Letter class
class Letter:
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
        self.font = pygame.font.SysFont(None, 36)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off the walls
        if self.x < 0 or self.x > screen_width:
            self.speed_x *= -1
        if self.y < 0 or self.y > screen_height:
            self.speed_y *= -1

    def draw(self):
        text_surface = self.font.render(self.char, True, RED)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

# Create letters for the word "HELLO"
letters = [Letter(char, random.randint(0, screen_width), random.randint(0, screen_height)) for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Move and draw each letter
    for letter in letters:
        letter.move()
        letter.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
