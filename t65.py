import turtle

# Function to draw a heart
def draw_heart(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(size)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(size)
    turtle.end_fill()

# Function to write a message
def write_message(x, y, message, font=("Arial", 16, "normal")):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(message, align="center", font=font)

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("pink")

# Draw heart
draw_heart(0, 50, 100, "red")

# Draw below heart part
turtle.color("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-35, 50)
turtle.pendown()
turtle.left(140)
turtle.circle(-50, 200)
turtle.left(120)
turtle.circle(-50, 200)
turtle.end_fill()

# Write message
write_message(0, -50, "Happy Mother's Day!", font=("Arial", 24, "bold"))

# Hide the turtle
turtle.done()
