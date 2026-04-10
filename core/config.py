"""Configuration module for parsing environment variables and storing app config."""

import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    """Configuration class storing loaded environment variables."""

    BASE_URL: str = os.getenv("BASE_URL", "https://api.restful-api.dev")


config: Config = Config()
