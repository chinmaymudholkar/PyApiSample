"""Utility module for log masking and other helper functions."""

import logging
import re
import sqlite3
import threading
from typing import Any

from core.constants import SENSITIVE_KEYS


class SQLiteHandler(logging.Handler):
    """Logging handler that writes to an SQLite database."""

    def __init__(self, db_path: str) -> None:
        """Initialize the SQLite logging handler.

        Args:
            db_path: The filesystem path to the SQLite database.

        """
        super().__init__()
        self.db_path = db_path
        self._lock = threading.Lock()
        self._init_db()

    def _init_db(self) -> None:
        """Initialize the database schema."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS logs ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,"
                "logger_name TEXT,"
                "level TEXT,"
                "message TEXT"
                ")",
            )

    def emit(self, record: logging.LogRecord) -> None:
        """Save a log record to the database."""
        try:
            msg = self.format(record)
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO logs (logger_name, level, message) VALUES (?, ?, ?)",
                    (record.name, record.levelname, msg),
                )
        except sqlite3.Error, RuntimeError:
            self.handleError(record)


class LogMasker:
    """Utility class to mask sensitive information in logs."""

    @classmethod
    def redact_data(cls, data: Any) -> Any:
        """Recursively mask sensitive keys in dictionaries or lists."""
        if isinstance(data, dict):
            return {
                k: (
                    "***REDACTED***"
                    if str(k).lower() in SENSITIVE_KEYS
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
            r"(Bearer\s+)[a-zA-Z0-9\-._~+/]+=*",
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
