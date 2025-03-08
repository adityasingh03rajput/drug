import pubchempy as pcp
import time

def query_pubchem(features):
    try:
        # Convert features to a query string (simplified for example)
        query = " ".join(map(str, features))
        
        # Query PubChem
        compounds = pcp.get_compounds(query, namespace="smiles", limit=1)
        time.sleep(1)  # Add a delay to avoid rate limits
        
        if compounds:
            return compounds[0]  # Return the first match
        return None
    except pcp.BadRequestError as e:
        print(f"PubChem API Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
