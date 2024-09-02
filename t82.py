import turtle
import math

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

# Function to draw flowers along the boundary of the heart
def draw_flower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(6):
        turtle.circle(10, 60)
        turtle.left(120)
    turtle.end_fill()

# Function to display Mother's Day message
def display_message():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Happy Mother's Day", align="center", font=("Arial", 20, "bold"))

# Function to clear the Mother's Day message
def clear_message():
    turtle.clear()

# Function to handle click event
def handle_click(x, y):
    global is_open
    if not is_open:
        draw_heart()
        for angle in range(0, 360, 30):
            x = 150 * math.cos(math.radians(angle))
            y = 150 * math.sin(math.radians(angle))
            draw_flower(x, y)
        display_message()
    else:
        turtle.clear()
        draw_heart()
        for angle in range(0, 360, 30):
            x = 150 * math.cos(math.radians(angle))
            y = 150 * math.sin(math.radians(angle))
            draw_flower(x, y)
    is_open = not is_open

# Set up the turtle screen
turtle.setup(width=600, height=600)
turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

# Register click event handler
turtle.onscreenclick(handle_click)

is_open = False

# Draw the heart initially
draw_heart()
for angle in range(0, 360, 30):
    x = 150 * math.cos(math.radians(angle))
    y = 150 * math.sin(math.radians(angle))
    draw_flower(x, y)

# Main loop
turtle.mainloop()
