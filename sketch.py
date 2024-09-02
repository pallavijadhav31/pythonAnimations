import cv2

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

# Create the sketch by combining the inverted blurred image with the original grayscale image
sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# Display the original image and the sketch
cv2.imshow("Original Image", image)
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
