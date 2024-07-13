from uuid import uuid4

from httpx import AsyncClient


class HttpClient:
    """An HTTP client that can be used to make requests to a server. Uses the `httpx` AyncClient library."""

    _client: AsyncClient = None
    _instances: dict[str, AsyncClient] = None

    def __init__(self, base_url: str, headers: dict[str, str] | None = None):
        self.base_url = base_url
        self.headers = headers
        self._client = AsyncClient()
        self._instances[str(uuid4())] = self._client

    def get(self, path: str, params: dict[str, str] | None = None) -> None:
        self._client.get(self.base_url + path, headers=self.headers, params=params)
