from decimal import Decimal


def full_kelly_fraction(probability: Decimal, decimal_odds: Decimal) -> Decimal:
    if not Decimal("0") < probability < Decimal("1"):
        raise ValueError("probability must be between 0 and 1")
    if decimal_odds <= 1:
        raise ValueError("decimal_odds must be > 1")

    b = decimal_odds - Decimal("1")
    q = Decimal("1") - probability
    fraction = (b * probability - q) / b
    return max(Decimal("0"), fraction)


def fractional_kelly(
    probability: Decimal,
    decimal_odds: Decimal,
    multiplier: Decimal = Decimal("0.20"),
) -> Decimal:
    return full_kelly_fraction(probability, decimal_odds) * multiplier
