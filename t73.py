import turtle
import random

# Function to draw text in chalk style
def draw_chalk_text(text, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.write(text, align="center", font=("Chalkduster", size, "normal"))

# Function to draw a chalk-like flower
def draw_chalk_flower(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("pink")
    turtle.begin_fill()
    for _ in range(6):
        turtle.circle(size, 60)
        turtle.right(120)
    turtle.end_fill()

# Function to draw sparkling particles
def draw_sparkle(x, y, color, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")

# Draw chalk-like text
draw_chalk_text("Happy Mother's Day", 0, 100, 40)

# Draw chalk-like flowers
for _ in range(10):
    x = random.randint(-int(turtle.window_width() / 2), int(turtle.window_width() / 2))
    y = random.randint(-int(turtle.window_height() / 2), int(turtle.window_height() / 2))
    size = random.randint(10, 30)
    draw_chalk_flower(x, y, size)

# Draw sparkling particles
for _ in range(50):
    x = random.randint(-int(turtle.window_width() / 2), int(turtle.window_width() / 2))
    y = random.randint(-int(turtle.window_height() / 2), int(turtle.window_height() / 2))
    size = random.randint(1, 5)
    color = random.choice(["yellow", "red", "orange"])
    draw_sparkle(x, y, color, size)

# Hide the turtle
turtle.done()
