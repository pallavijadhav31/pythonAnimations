import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os

def create_greeting_card():
    # Create a new blank image for the card
    width, height = 400, 300
    card = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(card)
    
    # Draw a colored rectangle as background
    draw.rectangle([(0, 0), (width, height)], fill="lightblue")
    
    # Load a font for text
    font_path = "arial.ttf"  # Change this to your font file path
    font = ImageFont.truetype(font_path, 20)
    
    # Add a greeting message
    greeting = "Happy Birthday!"
    text_width, text_height = font.getsize(greeting)
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(text_position, greeting, fill="black", font=font)
    
    # Add decorations (e.g., balloons, confetti, etc.)
    # Example: Draw some balloons
    draw.ellipse([(50, 50), (100, 100)], fill="red")
    draw.ellipse([(150, 100), (200, 150)], fill="blue")
    draw.ellipse([(250, 50), (300, 100)], fill="green")
    
    # Save the card
    card.save("greeting_card.png")

    # Open the saved card
    os.system("start greeting_card.png")  # Opens the image with the default image viewer on Windows

# Create the greeting card when the script is run
create_greeting_card()
