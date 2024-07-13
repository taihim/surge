from typing import ClassVar
from uuid import uuid4

from httpx import AsyncClient
from httpx._models import Response as HttpResponse


class HttpClient:
    """An HTTP client that can be used to make requests to a server. Uses the `httpx` AyncClient library."""

    _client: AsyncClient | None = None
    _instances: ClassVar[dict[str, "HttpClient"]] = {}

    def __repr__(self) -> str:
        """Returns a string representation of the client."""
        return f"<VektorClient base_url={self.base_url} id={self.client_id}>"

    def __init__(
        self, client_id: str, base_url: str, headers: dict[str, str] | None = None, timeout: float = 5.0
    ) -> None:
        """Initializes the client with the base URL and headers.

        Args:
            client_id: The ID of the client.
            base_url: The base URL of the server.
            headers: The headers to be sent with the request. Defaults to None.
            timeout: The timeout for the request. Defaults to 5.0.
        """
        self.base_url = base_url
        self.headers = headers
        self.client_id = client_id
        self._client = AsyncClient(timeout=timeout)

    @classmethod
    def get_or_create_instance(
        cls,
        client_id: str | None = None,
        base_url: str = "",
        headers: dict[str, str] | None = None,
        timeout: float = 5.0,
    ) -> "HttpClient":
        """Gets or creates an instance of the client.

        Args:
            client_id: The ID of the client. Defaults to None.
            base_url: The base URL of the server. Defaults to "".
            headers: The headers to be sent with the request. Defaults to None.
            timeout: The timeout for the request. Defaults to 5.0.

        Returns:
            An instance of HttpClient.
        """
        if not client_id:
            client_id = str(uuid4())

        if client_id not in cls._instances:
            cls._instances[client_id] = HttpClient(client_id, base_url, headers, timeout)

        return cls._instances[client_id]

    async def get(self, path: str, query_params: dict[str, str] | None = None) -> HttpResponse:
        """Makes a GET request to the server.

        Args:
            path: The path to make the request to.
            query_params: The query parameters to be sent with the request. Defaults to None.
        """
        if self._client:
            return await self._client.get(self.base_url + path, headers=self.headers, params=query_params)

        raise ValueError("Client not initialized")
