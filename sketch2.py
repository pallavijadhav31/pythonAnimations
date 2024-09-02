import cv2
import numpy as np
import time

# Load the image
image = cv2.imread("bear.png")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray_image = 255 - gray_image

# Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

# Invert the blurred image
inverted_blurred_image = 255 - blurred_image

# Create a blank canvas to draw the sketch
canvas = np.ones_like(image) * 255

# Create a VideoWriter object to save the sketching process as a video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('sketching_process.mp4', fourcc, 10.0, (image.shape[1], image.shape[0]))

# Draw the sketch step by step
for i in range(0, 255, 5):
    # Create the sketch by combining the inverted blurred image with the original grayscale image
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=i)
    
    # Draw the sketch on the canvas
    canvas[:, :, 0] = sketch
    canvas[:, :, 1] = sketch
    canvas[:, :, 2] = sketch
    
    # Display the sketching process
    cv2.imshow("Sketching Process", canvas)
    out.write(canvas)

    # Delay to visualize the sketching process
    time.sleep(0.5)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter object
out.release()

# Close all windows
cv2.destroyAllWindows()
