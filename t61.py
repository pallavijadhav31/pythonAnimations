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

# Function to draw a filled circle
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw a chocolate
def draw_chocolate(x, y, shape, size, color):
    if shape == "rectangle":
        draw_rectangle(x - size / 2, y - size / 4, size, size / 2, color)
    elif shape == "circle":
        draw_circle(x, y, size / 2, color)

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("beige")

# Draw chocolates
chocolates = [
    {"x": -150, "y": 150, "shape": "rectangle", "size": 40, "color": "saddlebrown"},
    {"x": 0, "y": 150, "shape": "circle", "size": 40, "color": "saddlebrown"},
    {"x": 150, "y": 150, "shape": "rectangle", "size": 40, "color": "saddlebrown"},
    {"x": -150, "y": 0, "shape": "circle", "size": 40, "color": "saddlebrown"},
    {"x": 0, "y": 0, "shape": "rectangle", "size": 40, "color": "saddlebrown"},
    {"x": 150, "y": 0, "shape": "circle", "size": 40, "color": "saddlebrown"},
    {"x": -150, "y": -150, "shape": "rectangle", "size": 40, "color": "saddlebrown"},
    {"x": 0, "y": -150, "shape": "circle", "size": 40, "color": "saddlebrown"},
    {"x": 150, "y": -150, "shape": "rectangle", "size": 40, "color": "saddlebrown"}
]

for chocolate in chocolates:
    draw_chocolate(chocolate["x"], chocolate["y"], chocolate["shape"], chocolate["size"], chocolate["color"])

# Hide the turtle
turtle.done()
