from decimal import Decimal

from src.pricing.math import (
    expected_value,
    implied_probability,
    minimum_executable_odds,
    proportional_no_vig,
)
from src.risk.sizing import fractional_kelly


def test_implied_probability() -> None:
    assert implied_probability(Decimal("2.00")) == Decimal("0.5")


def test_no_vig_sums_to_one() -> None:
    probabilities = proportional_no_vig([Decimal("1.91"), Decimal("1.91")])
    assert abs(sum(probabilities) - Decimal("1")) < Decimal("0.0000001")


def test_expected_value() -> None:
    assert expected_value(Decimal("0.52"), Decimal("2.02")) == Decimal("0.0504")


def test_minimum_executable_odds() -> None:
    assert minimum_executable_odds(Decimal("0.55"), Decimal("0.025")) > Decimal("1.86")


def test_fractional_kelly_never_negative() -> None:
    assert fractional_kelly(Decimal("0.40"), Decimal("2.00")) == Decimal("0")
