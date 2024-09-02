import turtle

# Function to draw a circle
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
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

# Function to draw the teddy bear
def draw_teddy_bear():
    # Head
    draw_circle(0, 100, 50, "brown")

    # Ears
    draw_circle(-40, 150, 15, "brown")
    draw_circle(40, 150, 15, "brown")

    # Eyes
    draw_circle(-20, 120, 5, "black")
    draw_circle(20, 120, 5, "black")

    # Nose
    draw_circle(0, 100, 7, "black")

    # Body
    draw_rectangle(-30, 50, 60, 80, "brown")

    # Arms
    draw_rectangle(-50, 70, 20, 50, "brown")
    draw_rectangle(30, 70, 20, 50, "brown")

    # Legs
    draw_rectangle(-20, -30, 20, 50, "brown")
    draw_rectangle(0, -30, 20, 50, "brown")

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("lightblue")

# Draw the teddy bear
draw_teddy_bear()

# Hide the turtle
turtle.done()
