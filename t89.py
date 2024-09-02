import turtle

# Function to draw the letters "Mother's Day"
def draw_mothers_day():
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    turtle.write("M", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.write("o", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.write("t", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write("h", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(50, 0)
    turtle.pendown()
    turtle.write("e", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.write("r", font=("Arial", 36, "bold"))
    turtle.penup()d
    turtle.goto(150, 0)
    turtle.pendown()
    turtle.write("'s", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    turtle.write("D", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(250, 0)
    turtle.pendown()
    turtle.write("a", font=("Arial", 36, "bold"))
    turtle.penup()
    turtle.goto(300, 0)
    turtle.pendown()
    turtle.write("y", font=("Arial", 36, "bold"))

# Set up the turtle screen
turtle.setup(width=800, height=200)
turtle.bgcolor("white")
turtle.speed(0)

# Draw "Mother's Day"
draw_mothers_day()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.mainloop()
