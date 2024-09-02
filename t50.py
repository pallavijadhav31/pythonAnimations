import turtle
import random

# Function to draw a single letter
def draw_letter(letter, x, y, color, font_size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.write(letter, font=("Arial", font_size, "bold"))

# Function to animate a name
def animate_name(name, x, y):
    turtle.speed(1)  # Set the animation speed
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.bgcolor("black")  # Set background color to black
    
    # Styling options
    font_sizes = [20, 30, 40, 50, 60]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    # Draw each letter with random color and font size
    for letter in name:
        font_size = random.choice(font_sizes)
        color = random.choice(colors)
        draw_letter(letter, x, y, color, font_size)
        x += font_size  # Adjust x position based on font size

# Main function
def main():
    name = "Pallavi"
    x = -200  # Initial x position
    y = 0     # Initial y position
    animate_name(name, x, y)
    
    turtle.done()  # Finish the drawing

# Run the main function
if __name__ == "__main__":
    main()
