from unittest.mock import AsyncMock, Mock, patch

from vektor.http_client import HttpClient


def test_get_or_create_instance_returning_singleton() -> None:
    instance_1 = HttpClient.get_or_create_instance()
    instance_2 = HttpClient.get_or_create_instance()
    instance_3 = HttpClient.get_or_create_instance("test_id")
    instance_4 = HttpClient.get_or_create_instance("test_id")

    assert instance_1 is not instance_2
    assert instance_3 is instance_4


@patch(
    "src.vektor.http_client.AsyncClient.get",
    return_value=Mock(status_code=200, headers={"Content-Type": "application/json"}, content=b"{}"),
)
async def test_get(mock_httpx_client: AsyncMock) -> None:
    client = HttpClient.get_or_create_instance()

    response = await client.get("https://httpbin.org/get")

    mock_httpx_client.assert_called_once_with("https://httpbin.org/get", headers=None, params=None)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.content is not None
    assert response.content == b"{}"


def test_repr() -> None:
    client = HttpClient.get_or_create_instance("test_id")
    assert repr(client) == "<VektorClient base_url= id=test_id>"
