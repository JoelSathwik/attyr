import numpy as np
from PIL import Image

def get_dominant_color(image_path):
    image = Image.open(image_path).convert("RGBA")
    image = np.array(image)

    # Flatten pixels
    pixels = image.reshape(-1, 4)

    # Keep visible pixels only
    pixels = pixels[pixels[:, 3] > 0][:, :3]

    if len(pixels) == 0:
        return "unknown"

    # Remove very dark pixels
    pixels = pixels[np.mean(pixels, axis=1) > 40]

    # Remove very bright pixels (near white)
    pixels = pixels[np.mean(pixels, axis=1) < 240]

    if len(pixels) == 0:
        return "unknown"

    avg_color = np.mean(pixels, axis=0)
    return rgb_to_color_name(avg_color)

def rgb_to_color_name(rgb):
    r, g, b = rgb

    if r > 200 and g > 200 and b > 200:
        return "white"
    if r < 60 and g < 60 and b < 60:
        return "black"

    if r > g and r > b:
        return "red"
    if g > r and g > b:
        return "green"
    if b > r and b > g:
        return "blue"

    if abs(r - g) < 20 and b < r:
        return "yellow"
    if abs(r - b) < 20 and g < r:
        return "purple"

    return "mixed"
