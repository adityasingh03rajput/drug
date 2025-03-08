import tensorflow as tf
import numpy as np

def extract_features(image):
    model = tf.keras.applications.EfficientNetB0(weights="imagenet", include_top=False, pooling="avg")
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    features = model.predict(image)
    return features.flatten()
