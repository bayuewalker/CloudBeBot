from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


TradingMode = Literal["SHADOW", "PULSE_ASSISTED", "PLAY_EUR", "API_LIVE"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    log_level: str = "INFO"

    cloudbet_api_key: str = ""
    cloudbet_base_url: str = "https://sports-api.cloudbet.com"

    trading_mode: TradingMode = "PULSE_ASSISTED"
    trading_currency: str = "PLAY_EUR"

    database_url: str = ""
    redis_url: str = ""


settings = Settings()
