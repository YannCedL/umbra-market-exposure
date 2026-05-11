from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def calculate_exposure(siren: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    contract.result = {
        "siren": siren,
        "exposure_score": 0.67,
        "sectors": {"defence": 0.45, "commercial_aviation": 0.35, "space": 0.20},
        "geographic_risk": {"europe": 0.60, "north_america": 0.25, "asia": 0.15}
    }
    contract.add_evidence(Evidence(subject=siren, predicate="market_exposure",
        value="0.67", source="financial_analysis", observed_at=now,
        confidence=0.85, status=EpistemicStatus.INFERENCE))
    return contract
