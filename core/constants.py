"""All the constants used across the code base."""
from enum import StrEnum


class HttpMethods(StrEnum):
    """All the HTTP methods supported by the code."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


SENSITIVE_KEYS: set[str] = {
    "password",
    "token",
    "access_token",
    "refresh_token",
    "authorization",
    "api_key",
    "apikey",
    "x-api-key",
    "secret",
    "client_secret",
    "cookie",
    "set-cookie",
}
