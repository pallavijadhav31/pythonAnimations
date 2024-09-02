import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flocking Simulation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Class for individual entities (boids)
class Boid:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
    
    def update(self, flock):
        cohesion = self.cohesion(flock)
        separation = self.separation(flock)
        alignment = self.alignment(flock)

        # Adjust velocity based on cohesion, separation, and alignment
        self.vx += cohesion[0] + separation[0] + alignment[0]
        self.vy += cohesion[1] + separation[1] + alignment[1]

        # Limit speed
        speed_limit = 2
        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > speed_limit:
            scale = speed_limit / speed
            self.vx *= scale
            self.vy *= scale

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Wrap around screen edges
        if self.x < 0:
            self.x = screen_width
        elif self.x > screen_width:
            self.x = 0
        if self.y < 0:
            self.y = screen_height
        elif self.y > screen_height:
            self.y = 0

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y)), 5)

    def cohesion(self, flock):
        # Compute center of mass of nearby boids
        center_of_mass = [0, 0]
        num_neighbors = 0
        for boid in flock:
            distance = math.sqrt((self.x - boid.x) ** 2 + (self.y - boid.y) ** 2)
            if 0 < distance < 50:  # Only consider boids within a certain radius
                center_of_mass[0] += boid.x
                center_of_mass[1] += boid.y
                num_neighbors += 1
        if num_neighbors > 0:
            center_of_mass[0] /= num_neighbors
            center_of_mass[1] /= num_neighbors
            dx = center_of_mass[0] - self.x
            dy = center_of_mass[1] - self.y
            return dx / 100, dy / 100
        else:
            return 0, 0

    def separation(self, flock):
        # Avoid collisions with nearby boids
        move_x = 0
        move_y = 0
        for boid in flock:
            distance = math.sqrt((self.x - boid.x) ** 2 + (self.y - boid.y) ** 2)
            if 0 < distance < 20:  # Only consider boids within a certain radius
                move_x += self.x - boid.x
                move_y += self.y - boid.y
        return move_x / 100, move_y / 100

    def alignment(self, flock):
        # Align velocity with nearby boids
        avg_vx = 0
        avg_vy = 0
        num_neighbors = 0
        for boid in flock:
            distance = math.sqrt((self.x - boid.x) ** 2 + (self.y - boid.y) ** 2)
            if 0 < distance < 50:  # Only consider boids within a certain radius
                avg_vx += boid.vx
                avg_vy += boid.vy
                num_neighbors += 1
        if num_neighbors > 0:
            avg_vx /= num_neighbors
            avg_vy /= num_neighbors
            return avg_vx / 8, avg_vy / 8
        else:
            return 0, 0

# Function to draw obstacles
def draw_obstacles(surface, obstacles):
    for obstacle in obstacles:
        pygame.draw.circle(surface, RED, (int(obstacle[0]), int(obstacle[1])), 10)

# Main loop
running = True
clock = pygame.time.Clock()

# Create flock of boids
flock_size = 50
flock = [Boid() for _ in range(flock_size)]

# Create obstacles
obstacles = [(200, 200), (400, 400), (600, 200)]

# Simulation loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update boids
    for boid in flock:
        boid.update(flock)

    # Clear the screen
    screen.fill(WHITE)

    # Draw obstacles
    draw_obstacles(screen, obstacles)

    # Draw boids
    for boid in flock:
        boid.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
