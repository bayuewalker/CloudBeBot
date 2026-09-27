import httpx

from src.config.settings import settings


class CloudbetClient:
    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        self._client = client or httpx.AsyncClient(
            base_url=settings.cloudbet_base_url,
            headers={"X-API-Key": settings.cloudbet_api_key},
            timeout=15.0,
        )

    async def get_sports(self) -> dict:
        response = await self._client.get("/pub/v2/odds/sports")
        response.raise_for_status()
        return response.json()

    async def get_event(self, event_id: str) -> dict:
        response = await self._client.get(f"/pub/v2/odds/events/{event_id}")
        response.raise_for_status()
        return response.json()

    async def get_currencies(self) -> dict:
        response = await self._client.get("/pub/v1/account/currencies")
        response.raise_for_status()
        return response.json()

    async def get_balance(self, currency: str) -> dict:
        response = await self._client.get(f"/pub/v1/account/currencies/{currency}/balance")
        response.raise_for_status()
        return response.json()

    async def place_straight(self, payload: dict) -> dict:
        response = await self._client.post("/pub/v4/bets/place/straight", json=payload)
        response.raise_for_status()
        return response.json()

    async def get_bets(self, params: dict | None = None) -> dict:
        response = await self._client.get("/pub/v4/bets", params=params)
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        await self._client.aclose()
