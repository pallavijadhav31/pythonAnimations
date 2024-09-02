import turtle
import random

# Function to draw a simple flower
def draw_flower(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(6):
        turtle.circle(size, 60)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y + size)
    turtle.pendown()
    turtle.color("green")
    turtle.circle(size / 2)

# Function to draw a daisy
def draw_daisy(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white", "yellow")
    turtle.begin_fill()
    for _ in range(12):
        turtle.forward(size)
        turtle.left(150)
    turtle.end_fill()

# Function to draw a sunflower
def draw_sunflower(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("brown", "yellow")
    turtle.begin_fill()
    for _ in range(36):
        turtle.forward(size)
        turtle.left(170)
    turtle.end_fill()

# Function to draw a rose
def draw_rose(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red", "pink")
    turtle.begin_fill()
    turtle.circle(size, 180)
    turtle.left(90)
    for _ in range(6):
        turtle.circle(size / 2, 120)
        turtle.left(60)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("lightblue")

# Draw flowers
flowers = [(random.randint(-200, 200), random.randint(-200, 200), random.randint(20, 100)) for _ in range(5)]
for x, y, size in flowers:
    draw_flower(x, y, size)
    draw_daisy(x + 50, y + 50, size)
    draw_sunflower(x - 50, y - 50, size)
    draw_rose(x + 50, y - 50, size)

# Hide the turtle
turtle.done()
