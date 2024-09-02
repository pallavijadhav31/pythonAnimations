import turtle
import random

# Function to draw a star in chalk-like style
def draw_star(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Function to draw cursive-like text using stars
def draw_cursive_text(text, x, y, size, color):
    spacing = 1.5 * size
    for char in text:
        if char.upper() in stars:
            draw_letter(char, x, y, size, color)
            x += spacing

# Function to draw a letter using stars
def draw_letter(letter, x, y, size, color):
    letter = letter.upper()  # Ensure uppercase
    stars = {
        'A': [(x - size, y + size * 2), (x - size * 0.5, y + size * 0.5), (x, y), (x + size * 0.5, y + size * 0.5), (x + size, y + size * 2)],
        'B': [(x, y), (x - size, y), (x - size, y + size), (x, y + size * 0.5), (x - size * 0.5, y + size), (x, y + size * 2), (x - size, y + size * 2), (x + size, y + size * 2)],
        'C': [(x + size, y + size * 2), (x - size, y + size * 2), (x, y + size * 2), (x - size, y), (x + size, y)],
        'D': [(x - size, y + size * 2), (x, y + size * 2), (x - size, y), (x + size, y), (x + size, y + size * 2)],
        'E': [(x, y), (x - size, y), (x, y + size * 0.5), (x - size, y + size), (x, y + size * 2), (x - size, y + size * 2), (x + size, y + size * 2)],
        'F': [(x, y), (x - size, y), (x, y + size * 0.5), (x - size, y + size), (x, y + size * 2), (x - size, y + size * 2)],
        'G': [(x + size, y + size * 2), (x - size, y + size * 2), (x, y + size * 2), (x + size, y), (x - size, y), (x + size, y + size)],
        'H': [(x - size, y), (x - size, y + size), (x, y + size * 0.5), (x + size, y + size), (x + size, y)],
        'I': [(x - size * 0.5, y), (x + size * 0.5, y), (x, y), (x, y + size * 2)],
        'J': [(x, y), (x - size, y), (x + size, y), (x + size, y + size * 2)],
        'K': [(x - size, y), (x - size, y + size * 2), (x, y + size), (x - size, y + size * 2), (x + size, y)],
        'L': [(x, y), (x - size, y), (x - size, y + size * 2)],
        'M': [(x - size, y), (x - size, y + size * 2), (x, y), (x + size, y + size * 2), (x + size, y)],
        'N': [(x - size, y), (x - size, y + size * 2), (x + size, y), (x + size, y + size * 2)],
        'O': [(x, y), (x - size, y), (x - size, y + size * 2), (x, y + size * 2), (x + size, y), (x + size, y + size * 2)],
        'P': [(x, y), (x - size, y), (x - size, y + size), (x, y + size * 0.5), (x - size * 0.5, y + size), (x, y + size * 2)],
        'Q': [(x, y), (x - size, y), (x - size, y + size * 2), (x, y + size * 2), (x + size, y), (x + size, y + size * 2), (x, y + size)],
        'R': [(x, y), (x - size, y), (x - size, y + size), (x, y + size * 0.5), (x - size * 0.5, y + size), (x, y + size * 2), (x - size, y + size * 2), (x + size, y + size * 2)],
        'S': [(x + size, y), (x - size, y), (x - size, y + size), (x, y + size * 0.5), (x - size, y + size * 2), (x, y + size * 2), (x + size, y + size * 2)],
        'T': [(x - size * 
