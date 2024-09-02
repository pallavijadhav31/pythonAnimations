import turtle

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

# Function to draw a chocolate bar
def draw_chocolate_bar():
    # Draw chocolate
    draw_rectangle(-50, -25, 100, 50, "saddlebrown")

    # Draw sections
    for i in range(-40, 50, 20):
        draw_rectangle(i, -25, 10, 50, "tan")

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("beige")

# Draw the chocolate bar
draw_chocolate_bar()

# Hide the turtle
turtle.done()
