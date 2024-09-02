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

# Function to draw a flower
def draw_flower(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(size * 0.5)
    turtle.end_fill()
    turtle.left(60)
    for _ in range(6):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        turtle.left(60)

# Function to draw a smiley
def draw_smiley(x, y, size):
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x - size / 2, y + size / 3)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(size / 3, 120)
    turtle.penup()
    turtle.goto(x + size / 2, y + size / 3)
    turtle.pendown()
    turtle.setheading(-120)
    turtle.circle(size / 3, 120)
    turtle.penup()
    turtle.goto(x - size / 2, y - size / 3)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(size / 6)
    turtle.penup()
    turtle.goto(x + size / 2, y - size / 3)
    turtle.pendown()
    turtle.circle(size / 6)

# Function to handle clicks
def click_handler(x, y):
    global hearts, flowers, smileys
    if -50 <= x <= 50 and -50 <= y <= 50:
        hearts.append(draw_heart(x, y, random.randint(20, 40), random.choice(["red", "pink", "purple"])))
        draw_glow(x, y, random.choice(["red", "pink", "purple"]))
    elif 150 <= x <= 250 and -50 <= y <= 50:
        flowers.append(draw_flower(x, y, random.randint(10, 20), random.choice(["red", "pink", "purple", "orange", "yellow"])))
        draw_glow(x, y, random.choice(["red", "pink", "purple", "orange", "yellow"]))
    elif -250 <= x <= -150 and -50 <= y <= 50:
        smileys.append(draw_smiley(x, y, random.randint(10, 20)))
        draw_glow(x, y, "yellow")

# Function to draw a glowing effect
def draw_glow(x, y, color):
    for i in range(5):
        turtle.penup()
        turtle.goto(x, y - i * 5)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(10 + i * 5)
        turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("lightblue")

# Draw clickable objects
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Register click event
turtle.onscreenclick(click_handler)

# Initialize lists to store drawn elements
hearts = []
flowers = []
smileys = []

# Main loop
turtle.mainloop()
