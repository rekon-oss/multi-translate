from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings, parse_obj_as


class FTSettings(BaseSettings):
    rest_url: Optional[AnyHttpUrl] = parse_obj_as(AnyHttpUrl, "http://localhost:8080")
    # graphql url
