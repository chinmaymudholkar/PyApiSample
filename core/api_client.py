"""Base API client module for HTTP operations."""

from typing import Any

import httpx

from core.config import config


class ApiClient:
    """A simple HTTP client wrapper for our test framework."""

    def __init__(self) -> None:
        """Initialize the API client from the environment config."""
        self.base_url: str = config.BASE_URL
        self.client: httpx.Client = httpx.Client(base_url=self.base_url)

    def get(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a GET request."""
        return self.client.get(endpoint, **kwargs)

    def post(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a POST request."""
        return self.client.post(endpoint, **kwargs)

    def put(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a PUT request."""
        return self.client.put(endpoint, **kwargs)

    def patch(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a PATCH request."""
        return self.client.patch(endpoint, **kwargs)

    def delete(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a DELETE request."""
        return self.client.delete(endpoint, **kwargs)

    def close(self) -> None:
        """Close the underlying HTTP client session."""
        self.client.close()


# Provide a global instance for tests
# Alternatively, tests can instantiate ApiClient themselves or use fixtures.
api_client: ApiClient = ApiClient()
