import turtle
import random

# Function to draw text
def draw_text(text, x, y, color, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", size, "bold"))

# Function to draw sparkles
def draw_sparkle(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Function to draw firecrackers
def draw_firecracker(x, y, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(height)
    turtle.right(135)
    turtle.forward(height / 2)
    turtle.right(90)
    turtle.forward(height / 2)
    turtle.right(135)
    turtle.forward(height)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()

# Draw blue sky background
turtle.bgcolor("#87CEEB")  # Sky Blue color

# Write "Happy Mother's Day" one letter at a time in pink
draw_text("H", -150, 0, "#FF69B4", 40)
draw_text("a", -100, 0, "#FF69B4", 40)
draw_text("p", -50, 0, "#FF69B4", 40)
draw_text("p", 0, 0, "#FF69B4", 40)
draw_text("y", 50, 0, "#FF69B4", 40)
draw_text(" ", 100, 0, "#FF69B4", 40)
draw_text("M", -150, -50, "#FF69B4", 40)
draw_text("o", -100, -50, "#FF69B4", 40)
draw_text("t", -50, -50, "#FF69B4", 40)
draw_text("h", 0, -50, "#FF69B4", 40)
draw_text("e", 50, -50, "#FF69B4", 40)
draw_text("r", 100, -50, "#FF69B4", 40)
draw_text("'", 150, -50, "#FF69B4", 40)
draw_text("s", 200, -50, "#FF69B4", 40)
draw_text(" ", 250, -50, "#FF69B4", 40)
draw_text("D", -150, -100, "#FF69B4", 40)
draw_text("a", -100, -100, "#FF69B4", 40)
draw_text("y", -50, -100, "#FF69B4", 40)

# Draw decorations (sparkles and firecrackers)
for _ in range(10):
    x = random.randint(-350, -300)
    y = random.randint(-200, 200)
    draw_sparkle(x, y, random.randint(5, 15))

for _ in range(5):
    x = random.randint(300, 350)
    y = random.randint(-200, 200)
    draw_firecracker(x, y, random.randint(50, 100))

# Hide the turtle
turtle.done()
