import turtle

# Function to draw a petal
def draw_petal(radius):
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.left(120)

# Function to draw a rose
def draw_rose(size):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -size)
    turtle.pendown()
    turtle.color("red", "pink")
    turtle.begin_fill()
    turtle.circle(size, 180)
    turtle.left(90)
    draw_petal(size/2)
    turtle.left(90)
    draw_petal(size/2)
    turtle.end_fill()

# Set up the turtle
turtle.hideturtle()
turtle.bgcolor("lightgreen")

# Draw the rose
draw_rose(100)

# Hide the turtle
turtle.done()
