import streamlit as st
from utils.image_utils import preprocess_image
from models.feature_extractor import extract_features
from database.pubchem_client import query_pubchem
from utils.display_utils import display_results

# Streamlit app
st.title("Drug Detection Machine")
st.write("Upload a microscopic image to analyze.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Preprocess the image
    image = preprocess_image(uploaded_file)
    
    # Extract features using a pretrained model
    features = extract_features(image)
    
    # Query PubChem for molecular data
    compound = query_pubchem(features)
    
    # Display results
    display_results(compound)
