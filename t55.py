import turtle
import random

# Function to draw a tree recursively
def draw_tree(trunk_length, trunk_width):
    if trunk_length < 5:  # Base case for recursion
        return
    else:
        # Draw trunk
        turtle.pensize(trunk_width)
        turtle.forward(trunk_length)
        turtle.left(30)
        draw_tree(trunk_length * 0.7, trunk_width * 0.6)  # Draw left branch
        turtle.right(60)
        draw_tree(trunk_length * 0.7, trunk_width * 0.6)  # Draw right branch
        turtle.left(30)
        turtle.backward(trunk_length)

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

# Draw tree
draw_tree(100, 10)

# Add some leaves
turtle.penup()
turtle.goto(-150, 50)
turtle.color("green")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(150, 50)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Hide turtle and display result
turtle.hideturtle()
turtle.done()
