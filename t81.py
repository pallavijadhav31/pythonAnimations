import turtle
import random

# Function to draw text
def draw_text(text, x, y, color, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", size, "bold"))

# Function to draw sparkles
def draw_sparkle(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Function to create balls
def create_ball(x, y, dx, dy, radius, color):
    ball = turtle.Turtle()
    ball.penup()
    ball.goto(x, y)
    ball.shape("circle")
    ball.shapesize(radius / 10)
    ball.color(color)
    ball.dx = dx
    ball.dy = dy
    return ball

# Function to move the balls
def move_balls():
    for ball in balls:
        x = ball.xcor()
        y = ball.ycor()
        x += ball.dx
        y += ball.dy
        ball.goto(x, y)
        # Check for collision with walls
        if x > 390 or x < -390:
            ball.dx *= -1
        if y > 290 or y < -290:
            ball.dy *= -1

# Function to handle mouse clicks
def handle_click(x, y):
    # Draw sparkles
    for _ in range(10):
        draw_sparkle(x, y, random.randint(5, 15))

# Set up the turtle screen
turtle.setup(width=800, height=600)
turtle.bgcolor("#87CEEB")  # Sky Blue color
turtle.title("Happy Mother's Day")

# Draw "Happy Mother's Day" in pink color
draw_text("Happy Mother's Day", 0, 200, "#FF69B4", 40)

# Register mouse click handler
turtle.onscreenclick(handle_click)

# Create balls
balls = []
for _ in range(5):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    dx = random.randint(-3, 3)
    dy = random.randint(-3, 3)
    radius = random.randint(10, 20)
    color = random.choice(["red", "orange", "yellow", "pink", "purple", "green", "blue"])
    balls.append(create_ball(x, y, dx, dy, radius, color))

# Main loop
while True:
    move_balls()
    turtle.update()
