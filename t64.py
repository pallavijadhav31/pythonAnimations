import turtle
import random

# Function to draw a heart
def draw_heart(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(size)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(size)
    turtle.end_fill()

# Function to draw a filled rectangle
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a filled circle
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("lightblue")

# Draw hearts
for _ in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(20, 50)
    color = random.choice(["red", "pink", "purple", "blue", "green"])
    draw_heart(x, y, size, color)

# Draw other shapes
for _ in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(20, 50)
    color = random.choice(["red", "pink", "purple", "blue", "green"])
    shape = random.choice(["rectangle", "circle"])
    if shape == "rectangle":
        draw_rectangle(x - size / 2, y - size / 2, size, size / 2, color)
    else:
        draw_circle(x, y, size / 2, color)

# Hide the turtle
turtle.done()
