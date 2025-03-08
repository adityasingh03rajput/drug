from PIL import Image
import numpy as np

def preprocess_image(file):
    image = Image.open(file).convert("RGB")
    image = image.resize((224, 224))  # Resize for model input
    image = np.array(image) / 255.0  # Normalize
    return image
