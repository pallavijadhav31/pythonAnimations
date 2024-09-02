import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Evolutionary Art Generator")

# Define colors
WHITE = (255, 255, 255)

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Class for individual shapes
class Shape:
    def __init__(self):
        self.shape_type = random.choice(['circle', 'rectangle'])
        self.color = random_color()
        self.size = random.randint(10, 100)
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        if self.shape_type == 'rectangle':
            self.width = random.randint(10, 100)
            self.height = random.randint(10, 100)
    
    def draw(self, surface):
        if self.shape_type == 'circle':
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
        elif self.shape_type == 'rectangle':
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# Function to calculate fitness based on similarity to a target image (placeholder)
def calculate_fitness(shape):
    # Placeholder: Use a simple distance metric
    target_image = pygame.Surface((screen_width, screen_height))
    target_color = random_color()
    target_size = random.randint(10, 100)
    pygame.draw.circle(target_image, target_color, (screen_width // 2, screen_height // 2), target_size)
    target_array = pygame.surfarray.array3d(target_image)
    shape_image = pygame.Surface((screen_width, screen_height))
    shape.draw(shape_image)
    shape_array = pygame.surfarray.array3d(shape_image)
    return np.sum(np.abs(target_array - shape_array))

# Function to select parents based on fitness (tournament selection)
def select_parents(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=lambda shape: shape.fitness)

# Function to perform crossover between parents to produce offspring
def crossover(parent1, parent2):
    child = Shape()
    if random.random() < 0.5:
        child.color = parent1.color
    else:
        child.color = parent2.color
    if random.random() < 0.5:
        child.size = parent1.size
    else:
        child.size = parent2.size
    if random.random() < 0.5:
        child.x = parent1.x
    else:
        child.x = parent2.x
    if random.random() < 0.5:
        child.y = parent1.y
    else:
        child.y = parent2.y
    if child.shape_type == 'rectangle':
        if random.random() < 0.5:
            child.width = parent1.width
        else:
            child.width = parent2.width
        if random.random() < 0.5:
            child.height = parent1.height
        else:
            child.height = parent2.height
    return child

# Function to mutate a shape
def mutate(shape, mutation_rate=0.1):
    if random.random() < mutation_rate:
        shape.color = random_color()
    if random.random() < mutation_rate:
        shape.size += random.randint(-10, 10)
    if random.random() < mutation_rate:
        shape.x += random.randint(-10, 10)
    if random.random() < mutation_rate:
        shape.y += random.randint(-10, 10)
    if shape.shape_type == 'rectangle':
        if random.random() < mutation_rate:
            shape.width += random.randint(-10, 10)
        if random.random() < mutation_rate:
            shape.height += random.randint(-10, 10)

# Main loop
running = True
clock = pygame.time.Clock()

# Generate initial population
population_size = 10
population = [Shape() for _ in range(population_size)]

# Evolutionary loop
generation = 1
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate fitness for each shape
    for shape in population:
        shape.fitness = calculate_fitness(shape)

    # Select parents, perform crossover, and mutation to generate offspring
    new_population = []
    for _ in range(population_size):
        parent1 = select_parents(population)
        parent2 = select_parents(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population

    # Draw the best shape from the current generation
    best_shape = min(population, key=lambda shape: shape.fitness)
    screen.fill(WHITE)
    best_shape.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1)

    # Print information about the current generation
    print(f"Generation {generation}, Best Fitness: {best_shape.fitness}")
    generation += 1

# Quit Pygame
pygame.quit()
