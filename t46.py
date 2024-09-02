import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flock of Birds Simulation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Class for representing a bird
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2*math.pi)
        self.speed = random.uniform(1, 3)

    def update(self, flock):
        separation_radius = 50
        alignment_radius = 100
        cohesion_radius = 150
        separation_force = 0.03
        alignment_force = 0.01
        cohesion_force = 0.01

        separation_vector = [0, 0]
        alignment_vector = [0, 0]
        cohesion_vector = [0, 0]
        count_separation = 0
        count_alignment = 0
        count_cohesion = 0

        for other in flock:
            if other != self:
                distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
                if distance < separation_radius:
                    separation_vector[0] += self.x - other.x
                    separation_vector[1] += self.y - other.y
                    count_separation += 1
                if distance < alignment_radius:
                    alignment_vector[0] += math.cos(other.angle)
                    alignment_vector[1] += math.sin(other.angle)
                    count_alignment += 1
                if distance < cohesion_radius:
                    cohesion_vector[0] += other.x
                    cohesion_vector[1] += other.y
                    count_cohesion += 1

        if count_separation > 0:
            separation_vector[0] /= count_separation
            separation_vector[1] /= count_separation
            separation_vector_length = math.sqrt(separation_vector[0]**2 + separation_vector[1]**2)
            self.angle += separation_force * math.atan2(separation_vector[1], separation_vector[0]) / separation_vector_length

        if count_alignment > 0:
            alignment_vector[0] /= count_alignment
            alignment_vector[1] /= count_alignment
            alignment_angle = math.atan2(alignment_vector[1], alignment_vector[0])
            self.angle += alignment_force * (alignment_angle - self.angle)

        if count_cohesion > 0:
            cohesion_vector[0] /= count_cohesion
            cohesion_vector[1] /= count_cohesion
            cohesion_angle = math.atan2(cohesion_vector[1] - self.y, cohesion_vector[0] - self.x)
            self.angle += cohesion_force * (cohesion_angle - self.angle)

        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, surface):
        pygame.draw.polygon(surface, BLACK, [(self.x, self.y), (self.x - 10*math.cos(self.angle + math.pi/7), self.y - 10*math.sin(self.angle + math.pi/7)), (self.x - 10*math.cos(self.angle - math.pi/7), self.y - 10*math.sin(self.angle - math.pi/7))])

# Main loop
running = True
clock = pygame.time.Clock()

# Create a flock of birds
flock = [Bird(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(20)]

# Simulation loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update birds
    for bird in flock:
        bird.update(flock)

    # Clear the screen
    screen.fill(WHITE)

    # Draw birds
    for bird in flock:
        bird.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
