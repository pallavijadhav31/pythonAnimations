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

# Function to draw stem and leaves
def draw_stem_and_leaves():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("green")
    turtle.pensize(5)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.backward(40)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(80)
    turtle.backward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(80)
    turtle.penup()
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)

# Set up the turtle
turtle.hideturtle()
turtle.bgcolor("lightgreen")

# Draw the rose
draw_rose(100)

# Draw the stem and leaves
draw_stem_and_leaves()

# Hide the turtle
turtle.done()
