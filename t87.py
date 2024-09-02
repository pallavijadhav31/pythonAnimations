import turtle
import random

# Function to draw a leaf
def draw_leaf(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(size, 60)
    turtle.left(120)
    turtle.circle(size, 60)
    turtle.end_fill()

# Function to draw a stem
def draw_stem():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("green")
    turtle.width(10)
    turtle.setheading(90)
    turtle.forward(100)

# Function to draw a flower using leaves
def draw_flower():
    for _ in range(20):  # Draw 20 leaves for the flower
        x = random.randint(-30, 30)
        y = random.randint(-150, -100)
        draw_leaf(x, y, 20)  # Set leaf size to 20

# Set up the turtle screen
turtle.setup(width=600, height=600)
turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

# Draw the stem
draw_stem()

# Draw the flower
draw_flower()

# Keep the window open
turtle.mainloop()
