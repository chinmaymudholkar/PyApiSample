"""Configuration module for parsing environment variables and storing app config."""

import logging
import os

from dotenv import load_dotenv

from core.utils import LogMasker


class SensitiveFormatter(logging.Formatter):
    """Formatter that masks sensitive information in log messages."""

    def format(self, record: logging.LogRecord) -> str:
        """Override format to mask message and arguments."""
        message = super().format(record)
        return LogMasker.redact_string(message)


# Set up logging
handler = logging.FileHandler("logs/audit.log", mode="a")
handler.setFormatter(
    SensitiveFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
)

logging.basicConfig(
    level=logging.INFO,
    handlers=[handler],
)
logger = logging.getLogger(__name__)

# Load environment variables from the .env file
load_dotenv()


class Config:
    """Configuration class storing loaded environment variables."""

    BASE_URL: str = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")

    def __init__(self) -> None:
        """Validate configuration."""
        if not self.BASE_URL.startswith(("http://", "https://")):
            logger.warning(
                "BASE_URL does not start with http:// or https://: %s",
                self.BASE_URL,
            )


config: Config = Config()
