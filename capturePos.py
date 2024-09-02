import cv2

def get_click_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at position: ({x}, {y})")

# Example usage
image_path = "C:\\Users\\jadha\\pics\\original.jpg"

# Set up a window to display the image and capture mouse events
cv2.namedWindow("image")
cv2.setMouseCallback("image", get_click_position)

# Show the original image
image = cv2.imread(image_path)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
