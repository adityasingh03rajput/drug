import numpy as np
from models.feature_extractor import extract_features

def test_extract_features():
    dummy_image = np.random.rand(224, 224, 3)  # Random image
    features = extract_features(dummy_image)
    assert features.shape == (62720,)  # Example feature shape
