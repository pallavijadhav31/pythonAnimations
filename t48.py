import turtle
import random

# Function to draw a firecracker
def draw_firecracker(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(25)
        turtle.right(144)
    turtle.end_fill()

# Function to explode a firecracker
def explode_firecracker(x, y, color):
    for _ in range(10):
        new_x = x + random.randint(-20, 20)
        new_y = y + random.randint(-20, 20)
        draw_firecracker(new_x, new_y, color)

# Main function
def main():
    turtle.speed(0)  # Set the animation speed to the fastest
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.bgcolor("black")  # Set background color to black

    # Draw multiple firecrackers
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        color = random.choice(["red", "orange", "yellow", "white", "green", "blue", "purple"])
        draw_firecracker(x, y, color)

    # Explode each firecracker
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        color = random.choice(["red", "orange", "yellow", "white", "green", "blue", "purple"])
        explode_firecracker(x, y, color)

    turtle.done()  # Finish the drawing

# Run the main function
if __name__ == "__main__":
    main()
