from decimal import Decimal


def implied_probability(decimal_odds: Decimal) -> Decimal:
    if decimal_odds <= 1:
        raise ValueError("decimal_odds must be > 1")
    return Decimal("1") / decimal_odds


def proportional_no_vig(decimal_odds: list[Decimal]) -> list[Decimal]:
    if len(decimal_odds) < 2:
        raise ValueError("at least two outcomes are required")

    raw = [implied_probability(price) for price in decimal_odds]
    total = sum(raw, Decimal("0"))

    if total <= 0:
        raise ValueError("invalid implied probability total")

    return [probability / total for probability in raw]


def expected_value(fair_probability: Decimal, offered_odds: Decimal) -> Decimal:
    if not Decimal("0") < fair_probability < Decimal("1"):
        raise ValueError("fair_probability must be between 0 and 1")
    if offered_odds <= 1:
        raise ValueError("offered_odds must be > 1")

    return fair_probability * offered_odds - Decimal("1")


def minimum_executable_odds(
    fair_probability: Decimal,
    minimum_ev: Decimal,
) -> Decimal:
    if not Decimal("0") < fair_probability < Decimal("1"):
        raise ValueError("fair_probability must be between 0 and 1")

    return (Decimal("1") + minimum_ev) / fair_probability
