# import pygame
# import pygame.freetype

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Birthday Greeting Card")

# # Set up fonts
# pygame.freetype.init()
# font = pygame.freetype.Font(None, 100)

# # Set up colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# # Main loop
# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
        
#         # Clear the screen
#         screen.fill(WHITE)
        
#         # Render and draw "Happy Birthday" text
#         font.render_to(screen, (width//4, height//3), "Happy Birthday", BLACK, size=50)
        
#         # Update the display
#         pygame.display.flip()

#     # Quit Pygame
#     pygame.quit()

# if __name__ == "__main__":
#     main()


import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(WHITE)

    # Draw colorful hearts
    for _ in range(50):
        color = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA])
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.polygon(screen, color, [(x, y + 15), (x + 10, y), (x + 20, y + 15), (x + 10, y + 30)])

    # Draw small balls
    for _ in range(100):
        color = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA])
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(screen, color, (x, y), 3)

    # Draw "Happy Birthday" text
    font = pygame.font.Font(None, 64)
    text = font.render("Happy Birthday!", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
