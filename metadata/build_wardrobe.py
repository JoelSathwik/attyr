import os
import sys
import json

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from classification.classify import classify_image
from extract_color import get_dominant_color


SEGMENTED_DIR = "../segmented_images"
WARDROBE_PATH = "wardrobe.json"

wardrobe = []

images = [
    img for img in os.listdir(SEGMENTED_DIR)
    if img.lower().endswith(".png")
]

for img in images:
    img_path = os.path.join(SEGMENTED_DIR, img)

    garment_type = classify_image(img_path)
    color = get_dominant_color(img_path)

    wardrobe.append({
        "image": img_path,
        "type": garment_type,
        "color": color
    })

with open(WARDROBE_PATH, "w") as f:
    json.dump(wardrobe, f, indent=2)

print("Virtual wardrobe built successfully.")
