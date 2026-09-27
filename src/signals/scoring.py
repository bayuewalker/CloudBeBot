from dataclasses import dataclass


@dataclass(frozen=True)
class PulseScoreInput:
    edge_quality: float
    reference_agreement: float
    freshness: float
    liquidity: float
    steam_confirmation: float
    event_popularity: float


def pulse_score(value: PulseScoreInput) -> float:
    score = (
        0.35 * value.edge_quality
        + 0.20 * value.reference_agreement
        + 0.15 * value.freshness
        + 0.10 * value.liquidity
        + 0.10 * value.steam_confirmation
        + 0.10 * value.event_popularity
    )
    return max(0.0, min(100.0, score))
