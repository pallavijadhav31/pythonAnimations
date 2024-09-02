import turtle
import time

# Function to draw the bulb
def draw_bulb():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

# Function to turn the bulb on
def turn_on():
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    draw_bulb()
    turtle.end_fill()

# Function to turn the bulb off
def turn_off():
    turtle.fillcolor("white")
    turtle.begin_fill()
    draw_bulb()
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")

# Main animation loop
while True:
    turn_on()
    time.sleep(1)
    turn_off()
    time.sleep(1)
