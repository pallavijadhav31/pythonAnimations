# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Elephant Drawing")
# screen.setup(width=600, height=600)
# screen.bgcolor("white")

# # Create a turtle for drawing
# t = turtle.Turtle()
# t.speed(0)  # Set the fastest drawing speed
# t.color("black")

# # Function to draw a circle
# def draw_circle(color, radius, x, y):
#     t.penup()
#     t.fillcolor(color)
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# # Function to draw a rectangle
# def draw_rectangle(color, width, height, x, y):
#     t.penup()
#     t.fillcolor(color)
#     t.goto(x, y)
#     t.setheading(0)
#     t.pendown()
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(width)
#         t.right(90)
#         t.forward(height)
#         t.right(90)
#     t.end_fill()

# # Draw the elephant
# draw_circle("gray", 100, 0, 0)                  # Body
# draw_circle("gray", 60, -120, 0)                 # Head
# draw_rectangle("gray", 60, 100, -70, -50)        # Trunk
# draw_rectangle("gray", 40, 80, -140, -100)       # Left ear
# draw_rectangle("gray", 40, 80, 80, -100)         # Right ear
# draw_circle("black", 10, -40, 30)                # Left eye
# draw_circle("black", 10, 40, 30)                 # Right eye
# draw_circle("black", 5, -40, 30)                 # Left pupil
# draw_circle("black", 5, 40, 30)                  # Right pupil
# draw_circle("black", 30, -160, -20)              # Left tusk
# draw_circle("black", 30, 100, -20)               # Right tusk

# # Hide the turtle and display the result
# t.hideturtle()
# turtle.done()


import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Elephant Drawing")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.color("black")
t.pensize(2)

# Draw the body
t.penup()
t.goto(0, -200)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.circle(150)
t.end_fill()

# Draw the head
t.penup()
t.goto(-50, 50)
t.pendown()
t.setheading(45)
t.fillcolor("gray")
t.begin_fill()
t.circle(70, 180)
t.setheading(-45)
t.circle(-70, 180)
t.end_fill()

# Draw the eyes
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(x-5, y+10)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

draw_eye(-80, 90)
draw_eye(20, 90)

# Draw the tusks
def draw_tusk(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(angle)
    t.fillcolor("white")
    t.begin_fill()
    t.forward(80)
    t.circle(10, 90)
    t.forward(10)
    t.circle(10, 90)
    t.forward(80)
    t.end_fill()

draw_tusk(-60, 0, 0)
draw_tusk(10, 0, 180)

# Draw the legs
def draw_leg(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    t.setheading(0)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.end_fill()

draw_leg(-40, -200)
draw_leg(20, -200)
draw_leg(-60, -270)
draw_leg(0, -270)

# Draw the tail
t.penup()
t.goto(-150, -20)
t.pendown()
t.setheading(230)
t.pensize(5)
t.forward(100)

# Hide the turtle and display the result
t.hideturtle()
turtle.done()



# from PIL import Image

# # Open the image file
# image = Image.open("bear.png")

# # Display the image
# image.show()