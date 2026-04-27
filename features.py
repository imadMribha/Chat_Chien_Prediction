from PIL import Image
import numpy as np

def extract_rgb(image_path):
    """
    Extract the average RGB values from an image.
    Returns a tuple: (average_red, average_green, average_blue)
    """
    # Open the image, convert to RGB, and resize to a smaller size for faster processing
    img = Image.open(image_path).convert("RGB")
    img = img.resize((50,50))

    # Convert the image to a numpy array and calculate the average RGB values
    pixels = np.array(img)

    red_average = pixels[:, :, 0].mean()
    green_average = pixels[:, :, 1].mean()
    blue_average = pixels[:, :, 2].mean()

    return (red_average, green_average, blue_average)