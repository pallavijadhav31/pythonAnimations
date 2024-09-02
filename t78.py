import turtle
import random

# Function to draw a circle
def draw_circle(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

# Function to draw a square
def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x - size / 2, y - size / 2)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Draw circles and squares randomly across the screen
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    size = random.randint(10, 50)
    color = random.choice(["red", "orange", "yellow", "pink", "purple"])
    draw_circle(x, y, size, color)

for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    size = random.randint(10, 50)
    color = random.choice(["blue", "green", "cyan", "magenta", "purple"])
    draw_square(x, y, size, color)

# Keep the window open until it's closed manually
turtle.done()
