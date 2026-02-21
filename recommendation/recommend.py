import json
from itertools import product

import matplotlib.pyplot as plt
from PIL import Image

def show_outfit(outfit):
    images = []
    titles = []

    images.append(Image.open(outfit["top"]["image"]))
    titles.append(f"{outfit['top']['type']}")

    images.append(Image.open(outfit["bottom"]["image"]))
    titles.append(f"{outfit['bottom']['type']}")

    if "jacket" in outfit:
        images.append(Image.open(outfit["jacket"]["image"]))
        titles.append("jacket")

    plt.figure(figsize=(4 * len(images), 4))

    for i, img in enumerate(images):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img)
        plt.title(titles[i])
        plt.axis("off")

    plt.show()

WARDROBE_PATH = "../metadata/wardrobe.json"

def load_wardrobe():
    with open(WARDROBE_PATH, "r") as f:
        return json.load(f)

def color_compatible(c1, c2):
    neutral = ["black", "white", "gray"]

    if c1 in neutral or c2 in neutral:
        return True
    if c1 == c2:
        return True
    if (c1 == "blue" and c2 in ["black", "white"]) or \
       (c2 == "blue" and c1 in ["black", "white"]):
        return True

    return False

def recommend_outfits(wardrobe):
    shirts = [g for g in wardrobe if g["type"] in ["shirt", "tshirt"]]
    pants = [g for g in wardrobe if g["type"] == "pant"]
    jackets = [g for g in wardrobe if g["type"] == "jacket"]

    outfits = []

    # Shirt/T-shirt + Pant
    for top, bottom in product(shirts, pants):
        if color_compatible(top["color"], bottom["color"]):
            outfits.append({
                "top": top,
                "bottom": bottom
            })

    # Jacket layering
    layered_outfits = []
    for outfit in outfits:
        for jacket in jackets:
            if color_compatible(jacket["color"], outfit["top"]["color"]):
                layered = outfit.copy()
                layered["jacket"] = jacket
                layered_outfits.append(layered)

    return outfits + layered_outfits

if __name__ == "__main__":
    wardrobe = load_wardrobe()
    outfits = recommend_outfits(wardrobe)

    print(f"Found {len(outfits)} outfit recommendations:\n")

    for i, outfit in enumerate(outfits[:5], 1):
        print(f"Showing Outfit {i}")
        show_outfit(outfit)

