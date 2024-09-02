import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Smiley Face Drawing")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.color("black")

# Function to draw a circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a smile
def draw_smile():
    t.penup()
    t.goto(0, -100)
    t.setheading(90)
    t.pendown()
    t.circle(100, 180)

# Draw the smiley face
draw_circle("yellow", 100, 0, 0)  # Head
draw_circle("black", 10, -40, 120)  # Left eye
draw_circle("black", 10, 40, 120)   # Right eye
draw_circle("red", 15, 0, 80)       # Nose
draw_smile()                        # Mouth

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
