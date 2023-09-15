import os

from functools import lru_cache


class Settings:
    # FastAPI
    app_name: str = 'Currency Converter'
    debug: bool = bool(os.environ.get("DEBUG"))
    version: str = "0.1"

    # Currency
    currency_url: str = 'https://api.coingate.com/v2/rates/merchant'


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
