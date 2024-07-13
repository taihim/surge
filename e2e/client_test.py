import asyncio

from vektor.http_client import HttpClient


async def main() -> None:
    c1 = HttpClient.get_or_create_instance()
    c2 = HttpClient.get_or_create_instance()

    resp = await c1.get(path="https://httpbin.org/get", query_params={"image": "dishwasher.JPEG"})

    print(resp)


if __name__ == "__main__":
    asyncio.run(main())
