"""Main function for the surge application."""

import asyncio

import aiohttp


async def main() -> None:
    """Main function for the surge application."""
    async with aiohttp.ClientSession() as session, session.get("http://python.org") as response:
        print("Status:", response.status)
        print("Content-type:", response.headers["content-type"])

        html = await response.text()
        print("Body:", html[:15], "...")
    print("Hello, world!")


asyncio.run(main())
