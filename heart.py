import turtle
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Heart-shaped Gift Card")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()

# Function to draw a heart
def draw_heart():
    pen.goto(0, -200)
    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.forward(224)
    pen.end_fill()

# Function to write a message
def write_message(message):
    pen.color("white")
    pen.goto(0, 0)
    pen.write(message, align="center", font=("Arial", 20, "normal"))

# Animation: Heart beating
def beat_heart():
    for _ in range(2):
        pen.shapesize(1, 1, 1)
        time.sleep(0.2)
        pen.shapesize(1.05, 1.05, 1.05)
        time.sleep(0.2)

# Draw the heart
draw_heart()

# Write a message
write_message("Happy Birthday!")

# Animation loop
while True:
    beat_heart()

# Keep the window open
screen.mainloop()
