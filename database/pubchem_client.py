import pubchempy as pcp

def query_pubchem(features):
    try:
        # Convert features to a query string (simplified for example)
        query = " ".join(map(str, features))
        
        # Query PubChem
        compounds = pcp.get_compounds(query, namespace="smiles", limit=1)
        
        if compounds:
            return compounds[0]  # Return the first match
        return None
    except Exception as e:
        print(f"Error querying PubChem: {e}")
        return None
