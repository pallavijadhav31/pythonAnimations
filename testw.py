import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Colorful Spiral Animation")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Define colors for the spiral
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Function to draw a colorful spiral
def draw_spiral():
    for i in range(360):
        pen.color(colors[i % 6])
        pen.forward(i)
        pen.left(59)

# Call the function to draw the spiral
draw_spiral()

# Keep the window open
screen.mainloop()
