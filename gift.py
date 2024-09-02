import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Gift Box Drawing")
screen.setup(width=400, height=400)
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.color("black")

# Function to draw a square
def draw_square(color, size, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

# Function to draw a ribbon
def draw_ribbon():
    t.penup()
    t.goto(-50, 50)
    t.setheading(45)
    t.pendown()
    t.width(5)
    t.color("red")
    t.forward(70)
    t.backward(70)
    t.setheading(-45)
    t.forward(70)
    t.backward(70)

# Draw the gift box
draw_square("blue", 100, -50, -50)  # Box
draw_ribbon()                       # Ribbon

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
