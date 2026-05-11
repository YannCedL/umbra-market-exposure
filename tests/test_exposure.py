from umbra_market_exposure import calculate_exposure

def test_calculate_exposure():
    c = calculate_exposure("383474814")
    assert "exposure_score" in c.result
    assert 0 <= c.result["exposure_score"] <= 1
