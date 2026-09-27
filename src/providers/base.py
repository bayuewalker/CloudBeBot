from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol


@dataclass(frozen=True)
class ReferenceQuote:
    provider: str
    provider_event_id: str
    sport: str
    competition: str
    start_time: datetime
    home: str
    away: str
    market_type: str
    period: str
    line: Decimal | None
    outcome: str
    decimal_odds: Decimal
    observed_at: datetime


class ReferenceOddsProvider(Protocol):
    async def fetch_quotes(self) -> list[ReferenceQuote]:
        ...
