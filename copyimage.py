print('Hello')
from PIL import Image, ImageDraw, ImageFont

def write_names_on_image(image_path, names, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Choose a font and size
    font = ImageFont.load_default()
    font_size = 30
    
    # Prepare to draw on the image
    draw = ImageDraw.Draw(image)
    
    # Position to start writing names
    x, y = 122, 321
    
    draw.text((x, y), name, fill="Black", font=ImageFont.truetype("arial.ttf", font_size))
    # Write each name onto the image
    # for name in names:
    #     
    #     y += font_size + 5  # Move down for the next name
    
    # Save the modified image
    image.save(output_path)

# Example usage
image_path = "C:\\Users\\jadha\\pics\\original.jpg"
names = ["Suresh JI", "Pallavi ji", "Babal ji"]
# output_path_prefix = 

# write_names_on_image(image_path, names, output_path)

for i, name in enumerate(names):
    output_path = f"C:\\Users\\jadha\\pics\\{name}.jpg"
    write_names_on_image(image_path, name, output_path)
