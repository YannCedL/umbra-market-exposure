# test du moteur d'exposition aux risques Umbra
from umbra_market_exposure.exposure import calculate_exposure

def test_calculate_exposure():
    contract = calculate_exposure("383474814")
    assert contract is not None
    assert contract.result["exposure_score"] > 0
    assert len(contract.evidence) >= 1
