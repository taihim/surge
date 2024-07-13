from uuid import uuid4

from httpx import AsyncClient


class HttpClient:
    """An HTTP client that can be used to make requests to a server. Uses the `httpx` AyncClient library."""

    _client: AsyncClient = None
    _instances: dict[str, AsyncClient] = {None}

    def __init__(self, url: str, client_id: uuid4):
        self._client = AsyncClient()
        self._instances[client_id] = self._client

    def get(self, path: str, params: Dict[str, str] = None) -> Response:
        return requests.get(self.url + path, headers=self.headers, params=params)

    def post(self, path: str, data: Dict[str, str] = None) -> Response:
        return requests.post(self.url + path, headers=self.headers, data=data)

    def put(self, path: str, data: Dict[str, str] = None) -> Response:
        return requests.put(self.url + path, headers=self.headers, data=data)

    def delete(self, path: str) -> Response:
        return requests.delete(self.url + path, headers=self.headers)