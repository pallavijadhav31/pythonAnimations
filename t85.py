import turtle
import random

# Function to draw a small heart shape
def draw_small_heart():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(50)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(0.5)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(0.5)
    turtle.forward(50)
    turtle.end_fill()

# Function to draw small leaves
def draw_flower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")  # Change leaf color to green
    turtle.begin_fill()
    for _ in range(5):  # Draw 5 small hearts for each flower
        draw_small_heart()
        turtle.left(72)  # Rotate for the next heart
    turtle.end_fill()

# Function to display Mother's Day message
def display_message():
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Happy Mother's Day", align="center", font=("Arial", 20, "bold"))

# Set up the turtle screen
turtle.setup(width=600, height=600)
turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

# Display Mother's Day message
display_message()

# Draw flowers all over the screen
for _ in range(20):  # Draw 20 flowers
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw_flower(x, y)

# Keep the window open
turtle.mainloop()
