import turtle
import random

# Function to draw a butterfly
def draw_butterfly(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    # Draw left wing
    turtle.circle(size, 90)
    turtle.circle(size/2, 180)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.circle(size/2, 180)
    turtle.circle(size, 90)

    # Draw right wing
    turtle.left(180)
    turtle.circle(-size, 90)
    turtle.circle(-size/2, 180)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.circle(-size/2, 180)
    turtle.circle(-size, 90)

    turtle.end_fill()

# Function to handle clicks
def click(x, y):
    global butterflies
    for butterfly in butterflies:
        butterfly.setheading(random.randint(0, 360))
        butterfly.speed(random.randint(1, 10))

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("skyblue")
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(300)
    turtle.right(90)
turtle.end_fill()

# Draw button text
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("white")
turtle.write("Click to release butterflies", align="center", font=("Arial", 20, "bold"))

# Set up the butterflies
butterflies = []
for _ in range(10):
    butterfly = turtle.Turtle()
    butterfly.shape("turtle")
    butterfly.color("purple")
    butterfly.penup()
    butterfly.setx(random.randint(-300, 300))
    butterfly.sety(random.randint(-200, 200))
    butterflies.append(butterfly)

# Click event
turtle.onscreenclick(click)

# Main loop
while True:
    for butterfly in butterflies:
        butterfly.forward(2)
        if butterfly.xcor() > 300 or butterfly.xcor() < -300:
            butterfly.right(180)
        if butterfly.ycor() > 200 or butterfly.ycor() < -200:
            butterfly.right(180)
    turtle.update()
