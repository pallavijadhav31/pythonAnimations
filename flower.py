# import turtle
# import math

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Rose Drawing")
# screen.setup(width=600, height=600)
# screen.bgcolor("white")

# # Create a turtle for drawing
# t = turtle.Turtle()
# t.speed(0)  # Set the fastest drawing speed
# t.color("red")

# # Function to draw a petal
# def draw_petal():
#     t.circle(100, 60)
#     t.left(120)
#     t.circle(100, 60)

# # Function to draw a rose
# def draw_rose():
#     for _ in range(6):
#         draw_petal()
#         t.left(60)

# # Function to draw a stem
# def draw_stem():
#     t.color("green")
#     t.width(10)
#     t.penup()
#     t.goto(0, -100)
#     t.pendown()
#     t.setheading(270)
#     t.forward(200)

# # Function to draw leaves
# def draw_leaves():
#     t.color("green")
#     t.penup()
#     t.goto(0, -100)
#     t.pendown()
#     t.begin_fill()
#     t.setheading(90)
#     t.circle(50, 90)
#     t.setheading(180)
#     t.circle(50, 90)
#     t.end_fill()

# # Function to draw the entire rose
# def draw_whole_rose():
#     draw_rose()
#     draw_stem()
#     draw_leaves()

# # Draw the rose
# draw_whole_rose()

# # Hide the turtle and display the result
# t.hideturtle()
# turtle.done()


import cv2
import numpy as np

# Create a blank canvas
canvas = np.ones((600, 600, 3), dtype=np.uint8) * 255

# Draw a rose sketch
def draw_rose(canvas):
    # Draw petals
    for angle in range(0, 360, 30):
        x = int(300 + 150 * np.cos(np.deg2rad(angle)))
        y = int(300 + 150 * np.sin(np.deg2rad(angle)))
        cv2.circle(canvas, (x, y), 10, (0, 0, 255), -1)
    
    # Draw stem
    cv2.line(canvas, (300, 450), (300, 550), (0, 255, 0), 5)
    
    # Draw leaves
    cv2.ellipse(canvas, (250, 500), (50, 25), 45, 0, 180, (0, 255, 0), -1)
    cv2.ellipse(canvas, (350, 500), (50, 25), -45, 0, 180, (0, 255, 0), -1)

# Draw the rose sketch
draw_rose(canvas)

# Display the sketch
cv2.imshow("Rose Sketch", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
