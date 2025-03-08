import pubchempy as pcp

def query_pubchem(features):
    query = " ".join(map(str, features))  # Simplified for example
    compounds = pcp.get_compounds(query, namespace="smiles", limit=1)
    if compounds:
        return compounds[0]  # Return the first match
    return None
