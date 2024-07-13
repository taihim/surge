from uuid import uuid4

from httpx import AsyncClient


class VektorClient:
    """An HTTP client that can be used to make requests to a server. Uses the `httpx` AyncClient library."""

    _client: AsyncClient = None
    _instance: "VektorClient" = None

    def __init__(self, base_url: str, headers: dict[str, str] | None = None, timeout: float = 5.0) -> None:
        """Initializes the client with the base URL and headers.

        Args:
            base_url: The base URL of the server.
            headers: The headers to be sent with the request. Defaults to None.
            timeout: The timeout for the request. Defaults to 5.0.
        """
        self.base_url = base_url
        self.headers = headers
        self._client = AsyncClient(timeout=timeout)

    @classmethod
    def get_or_create_instance(cls, base_url: str | None = None, headers: dict[str, str] | None = None, timeout: float = 5.0) -> "VektorClient":
        """Gets or creates an instance of the client."""
        if not cls._instance:
            cls._instance = VektorClient(base_url, headers, timeout)

        return cls._instance

    def get(self, path: str, query_params: dict[str, str] | None = None) -> None:
        """Makes a GET request to the server.

        Args:
            path: The path to make the request to.
            query_params: The query parameters to be sent with the request. Defaults to None.
        """
        self._client.get(self.base_url + path, headers=self.headers, params=query_params)
