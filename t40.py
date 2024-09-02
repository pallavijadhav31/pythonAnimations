import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
cell_size = 20
num_cells_x = screen_width // cell_size
num_cells_y = screen_height // cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Randomized Maze Generation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Class for individual cells in the maze
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = [True, True, True, True]  # [top, right, bottom, left]

    def draw(self, surface):
        x = self.col * cell_size
        y = self.row * cell_size
        if self.visited:
            pygame.draw.rect(surface, WHITE, (x, y, cell_size, cell_size))
            if self.walls[0]:  # top wall
                pygame.draw.line(surface, BLACK, (x, y), (x + cell_size, y), 2)
            if self.walls[1]:  # right wall
                pygame.draw.line(surface, BLACK, (x + cell_size, y), (x + cell_size, y + cell_size), 2)
            if self.walls[2]:  # bottom wall
                pygame.draw.line(surface, BLACK, (x, y + cell_size), (x + cell_size, y + cell_size), 2)
            if self.walls[3]:  # left wall
                pygame.draw.line(surface, BLACK, (x, y), (x, y + cell_size), 2)
        else:
            pygame.draw.rect(surface, BLACK, (x, y, cell_size, cell_size))

# Function to get neighbors of a cell
def get_neighbors(cell):
    neighbors = []
    if cell.row > 0:
        neighbors.append(grid[cell.row - 1][cell.col])  # top neighbor
    if cell.col < num_cells_x - 1:
        neighbors.append(grid[cell.row][cell.col + 1])  # right neighbor
    if cell.row < num_cells_y - 1:
        neighbors.append(grid[cell.row + 1][cell.col])  # bottom neighbor
    if cell.col > 0:
        neighbors.append(grid[cell.row][cell.col - 1])  # left neighbor
    return neighbors

# Function to remove walls between two cells
def remove_walls(current, neighbor):
    if current.row == neighbor.row:  # neighbor is to the right or left
        if current.col < neighbor.col:  # neighbor is to the right
            current.walls[1] = False  # remove current's right wall
            neighbor.walls[3] = False  # remove neighbor's left wall
        else:  # neighbor is to the left
            current.walls[3] = False  # remove current's left wall
            neighbor.walls[1] = False  # remove neighbor's right wall
    else:  # neighbor is above or below
        if current.row < neighbor.row:  # neighbor is below
            current.walls[2] = False  # remove current's bottom wall
            neighbor.walls[0] = False  # remove neighbor's top wall
        else:  # neighbor is above
            current.walls[0] = False  # remove current's top wall
            neighbor.walls[2] = False  # remove neighbor's bottom wall

# Function to draw the maze
def draw_maze(surface):
    for row in grid:
        for cell in row:
            cell.draw(surface)
    pygame.display.flip()

# Main loop
running = True
clock = pygame.time.Clock()

# Create grid of cells
grid = [[Cell(row, col) for col in range(num_cells_x)] for row in range(num_cells_y)]
current_cell = grid[0][0]  # start from the top-left corner
stack = []

# Maze generation loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mark current cell as visited
    current_cell.visited = True

    # Draw the maze after visiting each cell
    draw_maze(screen)

    # Randomly choose an unvisited neighbor
    neighbors = get_neighbors(current_cell)
    unvisited_neighbors = [neighbor for neighbor in neighbors if not neighbor.visited]
    if unvisited_neighbors:
        neighbor = random.choice(unvisited_neighbors)
        stack.append(current_cell)
        remove_walls(current_cell, neighbor)
        current_cell = neighbor
    elif stack:
        current_cell = stack.pop()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
