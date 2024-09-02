import turtle

# Function to draw the letter "A"
def draw_A():
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.left(75)
    turtle.forward(150)
    turtle.right(150)
    turtle.forward(150)
    turtle.backward(75)
    turtle.right(105)
    turtle.forward(65)

# Set up the turtle screen
turtle.setup(width=400, height=400)
turtle.bgcolor("white")
turtle.speed(2)

# Draw the letter "A"
draw_A()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.mainloop()
