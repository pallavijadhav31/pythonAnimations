import turtle

# Function to draw a butterfly
def draw_butterfly(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    # Draw left wing
    turtle.circle(size, 90)
    turtle.circle(size/2, 180)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.circle(size/2, 180)
    turtle.circle(size, 90)

    # Draw right wing
    turtle.left(180)
    turtle.circle(-size, 90)
    turtle.circle(-size/2, 180)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.circle(-size/2, 180)
    turtle.circle(-size, 90)

    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("skyblue")

# Draw butterfly
draw_butterfly(0, 0, 50, "purple")

# Hide the turtle
turtle.done()
