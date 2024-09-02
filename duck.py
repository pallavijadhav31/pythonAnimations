import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Duck Drawing")
screen.setup(width=600, height=600)
screen.bgcolor("sky blue")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.color("black")
t.pensize(2)

# Function to draw a filled circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw an arc
def draw_arc(color, radius, extent, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius, extent)
    t.end_fill()

# Function to draw a duck body
def draw_body():
    draw_circle("yellow", 100, 0, -150)  # Body

# Function to draw a duck head
def draw_head():
    draw_circle("yellow", 50, -50, -75)  # Head
    draw_circle("black", 10, -30, -60)    # Left eye
    draw_circle("black", 10, -70, -60)    # Right eye

# Function to draw a duck beak
def draw_beak():
    t.penup()
    t.goto(-50, -100)
    t.pendown()
    t.setheading(-45)
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.end_fill()

# Function to draw a duck tail
def draw_tail():
    draw_arc("orange", 40, -180, 50, -200)  # Tail

# Draw the duck
draw_body()
draw_head()
draw_beak()
draw_tail()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
