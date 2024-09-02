import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Define a function to draw a circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw Doraemon's face
draw_circle("#0099FF", 100, 0, -100)  # Blue face
draw_circle("white", 90, 0, -110)  # White inside face
draw_circle("#000000", 8, -30, -30)  # Left eye
draw_circle("#000000", 8, 30, -30)  # Right eye
draw_circle("#FF0000", 12, 0, -45)  # Nose

# Draw Doraemon's ears
t.penup()
t.goto(40, -20)
t.pendown()
t.setheading(60)
t.begin_fill()
t.circle(-50, 120)
t.end_fill()

t.penup()
t.goto(-40, -20)
t.pendown()
t.setheading(120)
t.begin_fill()
t.circle(50, 120)
t.end_fill()

# Draw Doraemon's body
draw_circle("#0099FF", 130, 0, -250)  # Blue body
draw_circle("#FFFFFF", 120, 0, -250)  # White inside body

# Draw Doraemon's hands
t.penup()
t.goto(100, -200)
t.pendown()
t.setheading(60)
t.forward(40)
t.backward(40)
t.setheading(0)
t.forward(70)
t.backward(70)

t.penup()
t.goto(-100, -200)
t.pendown()
t.setheading(120)
t.forward(40)
t.backward(40)
t.setheading(180)
t.forward(70)
t.backward(70)

# Draw Doraemon's bell
draw_circle("#FFD700", 15, 0, -240)  # Yellow bell
t.penup()
t.goto(0, -235)
t.pendown()
t.color("#FFD700")
t.width(4)
t.setheading(270)
t.circle(15, -180)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()
