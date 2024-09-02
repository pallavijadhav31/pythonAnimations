import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Name")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (128, 0, 128)]

# Function to draw a single letter
def draw_letter(screen, font, letter, x, y, color):
    text_surface = font.render(letter, True, color)
    screen.blit(text_surface, (x, y))

# Function to animate a name with various styles
def animate_name(screen, font, name, x, y):
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(BLACK)  # Clear screen
        
        # Draw each letter with random color
        for i, letter in enumerate(name):
            color = random.choice(COLORS)
            draw_letter(screen, font, letter, x + i * 50, y, color)
        
        pygame.display.flip()  # Update display
        clock.tick(5)  # Limit to 5 frames per second
        
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Main function
def main():
    font = pygame.font.Font(None, 60)  # Load font
    name = "Styles"
    x = 100
    y = HEIGHT // 2
    animate_name(screen, font, name, x, y)

# Run the main function
if __name__ == "__main__":
    main()
