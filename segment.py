from rembg import remove
from PIL import Image
import os

INPUT_DIR = "raw_images"
OUTPUT_DIR = "segmented_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img_name in os.listdir(INPUT_DIR):
    if img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(INPUT_DIR, img_name)
        output_path = os.path.join(OUTPUT_DIR, img_name)

        image = Image.open(input_path)
        output = remove(image)
        base = os.path.splitext(img_name)[0]
        output.save(os.path.join(OUTPUT_DIR, base + ".png"))

print("Segmentation completed.")
