"""Common datatypes used across the vektor module."""
from typing import TypedDict


class HttpResponse(TypedDict):
    """A dictionary representing an HTTP response from the HttpClient."""

    status_code: int
    content: bytes
    headers: dict[str, str]
