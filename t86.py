import turtle
import random

# Function to draw a flower
def draw_flower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(6):  # Draw a hexagon for the flower base
        turtle.forward(30)
        turtle.right(60)
    turtle.end_fill()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(5):  # Draw five petals for the flower
        turtle.circle(20)
        turtle.right(144)
    turtle.end_fill()

# Function to draw a bouquet of flowers
def draw_bouquet():
    for _ in range(10):  # Draw 10 flowers for the bouquet
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        draw_flower(x, y)

# Set up the turtle screen
turtle.setup(width=600, height=600)
turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

# Draw the bouquet
draw_bouquet()

# Keep the window open
turtle.mainloop()
