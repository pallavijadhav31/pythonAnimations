import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Basic Animation")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(-200, 0)

# Define the animation function
def animate():
    for _ in range(10):
        pen.forward(20)
        pen.left(90)
        pen.forward(20)
        pen.right(90)

# Call the animation function
animate()

# Keep the window open
screen.mainloop()
