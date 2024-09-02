import turtle
import random

# Function to draw a single firework explosion
def draw_explosion(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(random.choice(colors))
    for _ in range(36):
        turtle.forward(100)
        turtle.right(170)

# Function to animate fireworks
def animate_fireworks():
    turtle.speed(0)  # Set the animation speed to the fastest
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.bgcolor("black")  # Set background color to black

    # Draw multiple fireworks
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-100, 200)  # Adjusted y coordinate range
        draw_explosion(x, y)

    turtle.done()  # Finish the drawing

# Main function
def main():
    global colors
    colors = ["red", "orange", "yellow", "white", "green", "blue", "purple"]
    animate_fireworks()

# Run the main function
if __name__ == "__main__":
    main()
