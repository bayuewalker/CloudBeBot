import asyncio


async def main() -> None:
    while True:
        # Phase 2 will run fair-value, EV and Pulse Score calculations.
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
