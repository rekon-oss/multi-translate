import pydantic
from enum import Enum
from typing import Optional
from pathlib import Path


class LogLevelEnum(Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"


class DatabaseSettings(pydantic.BaseSettings):
    postgres_dsn: pydantic.PostgresDsn
    db_connect_timeout_seconds: int = 10


class Settings(pydantic.BaseSettings):
    # logging
    log_level: LogLevelEnum = LogLevelEnum.INFO
    # microsoft
    microsoft_translator_subscription_key: Optional[str] = None
    microsoft_translator_endpoint: Optional[pydantic.HttpUrl] = None
    microsoft_translator_using_virtual_network: Optional[bool] = False
    microsoft_translator_region: Optional[str] = None
    # google
    google_svc_account_json_path: Optional[Path] = None
    google_parent_path: Optional[
        Path
    ] = None  # path of the project/location to apply the calls to
    google_endpoint: Optional[pydantic.HttpUrl] = pydantic.parse_obj_as(
        pydantic.HttpUrl, "https://translation.googleapis.com"
    )
    # yandex
    # papago
    # amazon transcribe
    # ibm watson
    # deep L