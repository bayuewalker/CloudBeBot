import asyncio

from src.cloudbet.client import CloudbetClient


async def main() -> None:
    client = CloudbetClient()
    try:
        while True:
            # Phase 1 will normalize and persist Cloudbet snapshots.
            await client.get_sports()
            await asyncio.sleep(30)
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
