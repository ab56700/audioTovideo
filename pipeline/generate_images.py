import os
import requests
from PIL import Image
from io import BytesIO

def generate_images(scenes, output_dir="images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    paths = []

    for i, scene in enumerate(scenes):
        prompt = f"Sketch Style Illustration for: {scene}"
        url = "https://image.pollinations.ai/prompt/" + prompt.replace(" ", "%20")

        try:
            r = requests.get(url, timeout=25)
            img = Image.open(BytesIO(r.content)).convert("RGB")

            file_path = os.path.join(output_dir, f"scene_{i}.jpg")
            img.save(file_path)

        except:
            # fallback grey img
            img = Image.new("RGB", (512, 512), color=(180, 180, 180))
            file_path = os.path.join(output_dir, f"scene_{i}.jpg")
            img.save(file_path)

        paths.append(file_path)

    return paths
