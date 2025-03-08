from PIL import Image
import numpy as np

def preprocess_image(file):
    # Open and resize the image
    image = Image.open(file).convert("RGB")
    image = image.resize((224, 224))  # Resize for EfficientNet input
    image = np.array(image)  # Convert to numpy array
    return image
