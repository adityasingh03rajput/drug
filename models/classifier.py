def classify_substance(compound):
    if compound:
        return f"✅ Identified as {compound.iupac_name}. Molecular Formula: {compound.molecular_formula}"
    return "❌ Not a drug. Likely Water or another substance."
