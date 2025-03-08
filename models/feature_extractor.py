import tensorflow as tf
import numpy as np

# Load a pretrained model (EfficientNet)
def extract_features(image):
    model = tf.keras.applications.EfficientNetB0(
        weights="imagenet",  # Pretrained on ImageNet
        include_top=False,   # Exclude the classification layer
        pooling="avg"        # Use global average pooling
    )
    # Preprocess the image for EfficientNet
    image = tf.keras.applications.efficientnet.preprocess_input(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    features = model.predict(image)
    return features.flatten()  # Flatten to 1D array
