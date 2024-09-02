import turtle
import random

# Function to draw heart shape
def draw_heart():
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.color('red', 'pink')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

# Function to draw small leaves
def draw_flower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("purple")  # Change leaf color to purple
    turtle.begin_fill()
    for _ in range(5):  # Draw 5 leaves for each flower
        draw_leaf(x, y)
        turtle.left(72)  # Rotate for the next leaf
    turtle.end_fill()

# Function to draw a single leaf
def draw_leaf(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("purple")  # Change leaf color to purple
    turtle.begin_fill()
    for _ in range(6):
        turtle.circle(10, 60)
        turtle.left(120)
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

# Draw the heart
draw_heart()

# Display Mother's Day message
display_message()

# Draw flowers all over the screen
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw_flower(x, y)

# Keep the window open
turtle.mainloop()
