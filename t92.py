import tkinter as tk
from PIL import ImageTk, Image

class DragAndDropApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drag and Drop App")

        # Create a canvas for dragging and dropping
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create a frame for holding small images
        self.image_frame = tk.Frame(self.master, width=100, height=400, bg="lightgray")
        self.image_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # Load small images
        self.images = []
        self.load_images()

        # Bind events for dragging
        self.canvas.bind("<ButtonPress-1>", self.on_drag_start)
        self.canvas.bind("<B1-Motion>", self.on_drag_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_drag_release)

        self.drag_data = {"item": None, "x": 0, "y": 0}

    def load_images(self):
        # Load images and display them on the image frame
        for i in range(1, 4):
            image_path = f"ice{i}.jpg"
            image = Image.open(image_path)
            image = image.resize((50, 50), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            label = tk.Label(self.image_frame, image=image)
            label.image = image  # Keep a reference to prevent garbage collection
            label.pack(pady=5)

            # Bind events for dragging
            label.bind("<Button-1>", self.on_image_click)

            self.images.append((image, label))

    def on_image_click(self, event):
        # Create a new image on the canvas when clicked
        image = event.widget.cget("image")
        self.canvas.create_image(event.x, event.y, anchor=tk.NW, image=image)

    def on_drag_start(self, event):
        # Begin drag-and-drop operation
        x, y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
        self.drag_data["x"] = x - event.x
        self.drag_data["y"] = y - event.y
        self.drag_data["item"] = event.widget

    def on_drag_motion(self, event):
        # Handle dragging motion
        x, y = event.x_root + self.drag_data["x"], event.y_root + self.drag_data["y"]
        self.canvas.coords(self.drag_data["item"], x, y)

    def on_drag_release(self, event):
        # End drag-and-drop operation
        self.drag_data["item"] = None

def main():
    root = tk.Tk()
    app = DragAndDropApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
