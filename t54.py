import turtle
import random

# Function to draw a flower
def draw_flower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)
    turtle.color("green")
    turtle.left(30)
    turtle.circle(20, 60)
    turtle.left(30)
    turtle.color("red")
    for _ in range(6):
        turtle.circle(20, 60)
        turtle.left(120)

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")

# Main animation loop
for _ in range(100):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw_flower(x, y)
