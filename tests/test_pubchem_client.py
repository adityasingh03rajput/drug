from database.pubchem_client import query_pubchem

def test_query_pubchem():
    dummy_features = [0.1, 0.2, 0.3]  # Example features
    compound = query_pubchem(dummy_features)
    assert compound is None or hasattr(compound, "iupac_name")
