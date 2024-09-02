import turtle

# Function to draw text in chalk style
def draw_chalk_text(text, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.write(text, align="center", font=("Chalkduster", size, "normal"))

# Function to draw a chalk-like flower
def draw_chalk_flower(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("pink")
    turtle.begin_fill()
    for _ in range(6):
        turtle.circle(size, 60)
        turtle.right(120)
    turtle.end_fill()

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")

# Draw chalk-like text
draw_chalk_text("Happy Mother's Day", 0, 100, 40)

# Draw chalk-like flowers
draw_chalk_flower(-150, -50, 20)
draw_chalk_flower(0, -50, 20)
draw_chalk_flower(150, -50, 20)

# Hide the turtle
turtle.done()
