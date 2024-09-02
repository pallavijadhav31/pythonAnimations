import turtle

# Function to draw a sunflower
def draw_sunflower():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

    for _ in range(18):
        draw_petal()
        turtle.right(20)

# Function to draw a petal
def draw_petal():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.end_fill()
    turtle.right(20)

# Set up the turtle
turtle.hideturtle()
turtle.bgcolor("skyblue")

# Draw the sunflower
draw_sunflower()

# Hide the turtle
turtle.done()
