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

# Function to open/close the card
def toggle_card(x, y):
    global is_open
    if is_open:
        close_card()
    else:
        open_card()

# Function to open the card
def open_card():
    global is_open
    is_open = True
    draw_chalk_text("Happy Mother's Day!", 0, 100, 40)
    for _ in range(10):
        x = random.randint(-int(turtle.window_width() / 2), int(turtle.window_width() / 2))
        y = random.randint(-int(turtle.window_height() / 2), int(turtle.window_height() / 2))
        size = random.randint(10, 30)
        draw_chalk_flower(x, y, size)
    for _ in range(50):
        x = random.randint(-int(turtle.window_width() / 2), int(turtle.window_width() / 2))
        y = random.randint(-int(turtle.window_height() / 2), int(turtle.window_height() / 2))
        size = random.randint(1, 5)
        color = random.choice(["yellow", "red", "orange"])
        draw_sparkle(x, y, color, size)

# Function to close the card
def close_card():
    turtle.clear()
    is_open = False

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
is_open = False

# Draw closed card
draw_chalk_text("Click to Open", 0, 0, 20)

# Register click event to toggle the card
turtle.onscreenclick(toggle_card)

# Keep the window open
turtle.mainloop()
