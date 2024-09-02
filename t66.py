import turtle
import random

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

# Function to draw a colorful ball
def draw_ball(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

# Function to handle mouse clicks
def sparkle(x, y):
    turtle.clear()
    turtle.bgcolor("pink")
    draw_heart(0, 50, 100, "red")
    write_message(0, -50, "Happy Mother's Day!", font=("Arial", 24, "bold"))
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(5, 15)
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
        draw_ball(x, y, size, color)

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("pink")
turtle.listen()
turtle.onscreenclick(sparkle)

# Initial drawing
draw_heart(0, 50, 100, "red")
write_message(0, -50, "Happy Mother's Day!", font=("Arial", 24, "bold"))

# Main loop
while True:
    for ball in turtle.turtles():
        ball.setheading(ball.heading() + 1)
        ball.forward(5)
        if ball.xcor() > turtle.window_width() / 2 or ball.xcor() < -turtle.window_width() / 2:
            ball.right(180)
        if ball.ycor() > turtle.window_height() / 2 or ball.ycor() < -turtle.window_height() / 2:
            ball.right(180)
    turtle.update()
