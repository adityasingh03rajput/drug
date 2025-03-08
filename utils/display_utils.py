import streamlit as st

def display_results(compound):
    if compound:
        st.success(f"✅ Identified as {compound.iupac_name}.")
        st.write(f"Molecular Formula: {compound.molecular_formula}")
    else:
        st.error("❌ Not a drug. Likely Water or another substance.")
