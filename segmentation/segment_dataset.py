import os
from rembg import remove
from PIL import Image

RAW_DATASET = "../dataset_raw"
OUTPUT_DATASET = "../dataset"

SPLITS = ["train", "val"]
CLASSES = ["shirt", "tshirt", "pant", "jacket"]
MAX_IMAGES_PER_CLASS = 100  # 🔹 LIMIT HERE

def segment_and_save(input_path, output_path):
    image = Image.open(input_path)
    output = remove(image)
    output.save(output_path)

for split in SPLITS:
    for cls in CLASSES:
        input_dir = os.path.join(RAW_DATASET, split, cls)
        output_dir = os.path.join(OUTPUT_DATASET, split, cls)

        os.makedirs(output_dir, exist_ok=True)

        if not os.path.exists(input_dir):
            print(f"Skipping missing folder: {input_dir}")
            continue

        images = [
            img for img in os.listdir(input_dir)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        # 🔹 LIMIT THE NUMBER OF IMAGES
        images = images[:MAX_IMAGES_PER_CLASS]

        print(f"Processing {split}/{cls} ({len(images)} images)")

        for img_name in images:
            input_img_path = os.path.join(input_dir, img_name)
            base_name = os.path.splitext(img_name)[0]
            output_img_path = os.path.join(output_dir, base_name + ".png")

            try:
                segment_and_save(input_img_path, output_img_path)
            except Exception as e:
                print(f"Failed on {input_img_path}: {e}")

print("\nDataset segmentation completed successfully.")
