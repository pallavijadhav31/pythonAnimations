import cv2
import numpy as np
from moviepy.editor import *

# Load the main GIF for the center
main_gif = VideoFileClip("hb.gif")

# Create a blank image with the same dimensions as the main GIF
blank_image = np.zeros((main_gif.size[1], main_gif.size[0], 3), np.uint8)

# Define parameters for sparkling paper-cutting celebration
num_sparkles = 100
sparkle_size = 10

# Generate random positions for sparkles
positions = np.random.randint(0, main_gif.size[0], size=(num_sparkles, 2))

# Create each frame
for t in range(int(main_gif.duration * main_gif.fps)):
    # Copy blank image for each frame
    frame = blank_image.copy()
    
    # Draw sparkles on the blank image
    for pos in positions:
        color = tuple(np.random.randint(0, 256, size=3).tolist())  # Convert to tuple of integers
        cv2.circle(frame, tuple(pos), sparkle_size, color, -1)
    
    # Combine the main GIF and the sparkling animation
    combined_frame = np.hstack((main_gif.get_frame(t/main_gif.fps), frame))

    # Display the frame
    cv2.imshow("Combined", combined_frame)
    cv2.waitKey(25)  # Adjust delay as needed (in milliseconds)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
