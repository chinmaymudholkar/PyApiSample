"""Base API client module for HTTP operations."""

import logging
from typing import Any

import httpx

from core.config import config
from core.constants import HttpMethods
from core.utils import LogMasker

logger = logging.getLogger(__name__)


class ApiClient:
    """A simple HTTP client wrapper for our test framework."""

    def __init__(self, *, raise_for_status: bool = False) -> None:
        """Initialize the API client from the environment config."""
        self.base_url: str = config.BASE_URL
        self.raise_for_status = raise_for_status
        self.client: httpx.Client = httpx.Client(base_url=self.base_url)
        logger.info("Initialized ApiClient with base_url: %s", self.base_url)

    def _request(
        self, method: HttpMethods, endpoint: str, **kwargs: Any
    ) -> httpx.Response:
        """Send an HTTP request and log it."""
        masked_json = LogMasker.redact_data(kwargs.get("json", ""))
        masked_headers = LogMasker.redact_data(kwargs.get("headers", {}))

        logger.info(
            "Request: %s %s headers=%s body=%s",
            method,
            endpoint,
            masked_headers,
            masked_json,
        )

        response = self.client.request(method, endpoint, **kwargs)

        try:
            response_json = response.json()
            masked_response_body = LogMasker.redact_data(response_json)
        except ValueError, KeyError:
            masked_response_body = LogMasker.redact_string(response.text)

        logger.info(
            "Response: %s %s body=%s",
            response.status_code,
            response.url,
            masked_response_body,
        )

        if self.raise_for_status:
            response.raise_for_status()
        return response

    def get(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a GET request."""
        return self._request(HttpMethods.GET, endpoint, **kwargs)

    def post(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a POST request."""
        return self._request(HttpMethods.POST, endpoint, **kwargs)

    def put(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a PUT request."""
        return self._request(HttpMethods.PUT, endpoint, **kwargs)

    def patch(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a PATCH request."""
        return self._request(HttpMethods.PATCH, endpoint, **kwargs)

    def delete(self, endpoint: str = "/", **kwargs: Any) -> httpx.Response:
        """Send a DELETE request."""
        return self._request(HttpMethods.DELETE, endpoint, **kwargs)

    def close(self) -> None:
        """Close the underlying HTTP client session."""
        self.client.close()
