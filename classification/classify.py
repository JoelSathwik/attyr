import torch
from PIL import Image
from .model_loader import load_model, transform
from .labels import LABELS
import os

SEGMENTED_DIR = "../segmented_images"

model = load_model()

def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        predicted = outputs.argmax(1).item()

    return LABELS.get(predicted, "unknown")

if __name__ == "__main__":
    if not os.path.exists(SEGMENTED_DIR):
        print("Segmented images folder not found.")
        exit()

    images = [
        img for img in os.listdir(SEGMENTED_DIR)
        if img.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if len(images) == 0:
        print("No images found in segmented_images.")
        exit()

    print("Classifying garments...\n")

    for img_name in images:
        img_path = os.path.join(SEGMENTED_DIR, img_name)
        label = classify_image(img_path)
        print(f"{img_name}  -->  {label}")
