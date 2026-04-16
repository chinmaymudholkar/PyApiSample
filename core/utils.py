"""Utility module for log masking and other helper functions."""

import re
from typing import Any, ClassVar


class LogMasker:
    """Utility class to mask sensitive information in logs."""

    SENSITIVE_KEYS: ClassVar[set[str]] = {
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

    @classmethod
    def redact_data(cls, data: Any) -> Any:
        """Recursively mask sensitive keys in dictionaries or lists."""
        if isinstance(data, dict):
            return {
                k: (
                    "***REDACTED***"
                    if str(k).lower() in cls.SENSITIVE_KEYS
                    else cls.redact_data(v)
                )
                for k, v in data.items()
            }
        if isinstance(data, list):
            return [cls.redact_data(item) for item in data]
        return data

    @classmethod
    def redact_string(cls, text: str) -> str:
        """Mask sensitive information in a string (e.g., Bearer tokens)."""
        # Mask Bearer tokens
        text = re.sub(
            r"(Bearer\s+)[a-zA-Z0-9\-\._~+/]+=*",
            r"\1***REDACTED***",
            text,
            flags=re.IGNORECASE,
        )
        # Mask basic auth
        return re.sub(
            r"(Basic\s+)[a-zA-Z0-9+/]+=*",
            r"\1***REDACTED***",
            text,
            flags=re.IGNORECASE,
        )
