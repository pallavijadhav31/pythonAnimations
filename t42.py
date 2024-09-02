import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
cell_size = 10
num_cells_x = 80
num_cells_y = 60
screen_width = cell_size * num_cells_x
screen_height = cell_size * num_cells_y
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Generator")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to initialize the grid with random values
def initialize_grid():
    grid = [[random.choice([0, 1]) for _ in range(num_cells_x)] for _ in range(num_cells_y)]
    return grid

# Function to apply the rules of the Game of Life cellular automaton
def apply_rules(grid):
    new_grid = [[0 for _ in range(num_cells_x)] for _ in range(num_cells_y)]
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            alive_neighbors = count_alive_neighbors(grid, x, y)
            if grid[y][x] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if alive_neighbors == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
    return new_grid

# Function to count the number of alive neighbors of a cell
def count_alive_neighbors(grid, x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            neighbor_x = x + dx
            neighbor_y = y + dy
            if neighbor_x >= 0 and neighbor_x < num_cells_x and neighbor_y >= 0 and neighbor_y < num_cells_y:
                count += grid[neighbor_y][neighbor_x]
    return count

# Function to draw the grid on the screen
def draw_grid(surface, grid):
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(surface, color, (x * cell_size, y * cell_size, cell_size, cell_size))

# Main loop
running = True
clock = pygame.time.Clock()

# Initialize the grid with random values
grid = initialize_grid()

# Simulation loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply the rules of the Game of Life
    grid = apply_rules(grid)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    draw_grid(screen, grid)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()
