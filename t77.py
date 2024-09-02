import turtle
import random

# Function to draw a flower
def draw_flower(x, y, size, petals, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(petals):
        turtle.circle(size)
        turtle.right(360 / petals)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a star
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

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Draw flowers and stars in different sections of the screen
for _ in range(10):
    x = random.randint(-300, -100)
    y = random.randint(-200, 200)
    size = random.randint(10, 50)
    petals = random.randint(5, 10)
    color = random.choice(["red", "orange", "yellow", "pink", "purple"])
    draw_flower(x, y, size, petals, color)

for _ in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-200, 200)
    size = random.randint(10, 30)
    color = random.choice(["blue", "green", "cyan", "magenta", "purple"])
    draw_star(x, y, size, color)

for _ in range(10):
    x = random.randint(100, 300)
    y = random.randint(-200, 200)
    size = random.randint(10, 50)
    petals = random.randint(5, 10)
    color = random.choice(["red", "orange", "yellow", "pink", "purple"])
    draw_flower(x, y, size, petals, color)

# Keep the window open until it's closed manually
turtle.done()
