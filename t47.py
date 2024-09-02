import pygame
import random
import math


# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Bursting Animation")

# Load popping sound
pop_sound = pygame.mixer.Sound("pop.wav")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Class for representing a bubble
class Bubble:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.dx = random.uniform(-speed, speed)
        self.dy = random.uniform(-speed, speed)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.dx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Main loop
running = True
clock = pygame.time.Clock()

# Create a list to hold the bubbles
bubbles = []

# Score
score = 0

# Simulation loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Create new bubbles occasionally
    if len(bubbles) < 10 and random.random() < 0.05:
        radius = random.randint(20, 50)
        x = random.randint(radius, screen_width - radius)
        y = random.randint(radius, screen_height - radius)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        speed = random.uniform(1, 3)
        bubbles.append(Bubble(x, y, radius, color, speed))

    # Update and draw bubbles
    for bubble in bubbles:
        bubble.move()
        bubble.draw(screen)

    # Check for bubble collisions
    for bubble in bubbles:
        for other in bubbles:
            if bubble != other:
                distance = math.sqrt((bubble.x - other.x)**2 + (bubble.y - other.y)**2)
                if distance < bubble.radius + other.radius:
                    pop_sound.play()
                    score += 1
                    if bubble.radius > 10:
                        bubble.radius //= 2
                        other.radius //= 2
                        bubble.dx *= 1.1
                        bubble.dy *= 1.1
                        other.dx *= 1.1
                        other.dy *= 1.1

    # Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
