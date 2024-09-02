import turtle

# Function to draw a circle of stars
def draw_star_circle(x, y, radius, num_stars):
    angle = 360 / num_stars
    for _ in range(num_stars):
        draw_star(x, y, 10, "black")
        turtle.penup()
        turtle.setposition(x, y)
        turtle.pendown()
        turtle.right(angle)

# Function to draw a star
def draw_star(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Draw circles of stars
draw_star_circle(0, 0, 100, 20)
draw_star_circle(0, 0, 150, 15)
draw_star_circle(0, 0, 200, 10)
draw_star_circle(0, 0, 250, 5)

# Keep the window open until it's closed manually
turtle.done()
