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

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("lightblue")

# Draw hearts
for _ in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(50, 100)
    color = random.choice(["red", "pink", "purple", "blue", "green"])
    draw_heart(x, y, size, color)

# Hide the turtle
turtle.done()
