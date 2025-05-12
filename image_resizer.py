from PIL import Image
import os

def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            img = img.resize(size)
            img.save(output_path)
        print(f"Image successfully resized to {size} and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_path = input("Enter the path of the image to resize: ")
    output_path = input("Enter the output path for the resized image: ")
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    size = (width, height)

    resize_image(input_path, output_path, size)
