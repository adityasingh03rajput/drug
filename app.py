import streamlit as st
from utils.image_utils import preprocess_image
from models.feature_extractor import extract_features
from database.pubchem_client import query_pubchem
from utils.display_utils import display_results

st.title("Drug Detection Machine")
st.write("Upload a microscopic image to analyze.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = preprocess_image(uploaded_file)
    features = extract_features(image)
    compound = query_pubchem(features)
    display_results(compound)
