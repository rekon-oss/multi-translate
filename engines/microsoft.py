import copy
import json
import logging
import uuid
from typing import Optional, List, Dict
from urllib.parse import urljoin

import httpx

from engines.base import BaseTranslationEngine
from errors import (
    TranslationEngineNotConfiguredError,
    DetectionError,
    TranslationError,
    EngineApiError,
    AlignmentError,
)
from models import TranslationResponse, Alignment
from settings import Settings


def parse_alignment_string(
        alignment_str: str, source_text: str, translation_text: str
) -> Alignment:
    alignment_list = []
    alignment_chunks = alignment_str.split(" ")
    for chunk in alignment_chunks:
        source_text_frame, translation_text_frame = chunk.split("-")
        source_text_start, source_text_end = source_text_frame.split(":")
        translation_text_start, translation_text_end = translation_text_frame.split(":")

        source_text_section = source_text[int(source_text_start): int(source_text_end) + 1]
        translation_text_section = translation_text[
                                   int(translation_text_start): int(translation_text_end) + 1
                                   ]
        alignment_list.append(
            {
                "src": {
                    "start": int(source_text_start),
                    "end": int(source_text_end),
                    "text": source_text_section,
                },
                "dest": {
                    "start": int(translation_text_start),
                    "end": int(translation_text_end),
                    "text": translation_text_section,
                },
            }
        )
    return alignment_list


class MicrosoftEngine(BaseTranslationEngine):
    NAME = "microsoft"
    VERSION = "3.0"

    def __init__(self):
        settings = Settings()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(settings.log_level.value)

        self.subscription_key = settings.microsoft_translator_subscription_key
        self.endpoint = settings.microsoft_translator_endpoint
        self.region_headers = {} if settings.microsoft_translator_region is None else {
            "Ocp-Apim-Subscription-Region": settings.microsoft_translator_region}
        self.virtual_network_on = settings.microsoft_translator_using_virtual_network
        super().__init__()

    def handle_api_error(self, response_json: Dict):
        if "error" in response_json:
            raise EngineApiError(
                f"{self.name_ver} engine returned error code: {response_json['error']['code']},"
                f" message: {response_json['error']['message']}"
            )

    def get_supported_translations(self) -> Dict[str, List[str]]:
        response = httpx.get(urljoin("https://api.cognitive.microsofttranslator.com/", "languages"),
                             params={"api-version": self.VERSION})
        response_json = response.json()
        self.handle_api_error(response_json)
        all_translations = response_json["translation"].keys()
        return {c: all_translations for c in all_translations}

    async def translate(
            self,
            source_text: str,
            to_language: str,
            from_language: Optional[str] = None,
            with_alignment: Optional[bool] = False,
    ) -> TranslationResponse:
        from_dict = {} if from_language is None else {"from": from_language}
        alignment_dict = {"includeAlignment": with_alignment}
        translate_url = urljoin(str(self.endpoint),
                                f"translator/text/v{self.VERSION}/translate" if self.virtual_network_on else "translate")
        self._logger.debug("making request to %s", translate_url)

        async with httpx.AsyncClient() as client:

            response = await client.post(translate_url,
                                         json=[{"text": source_text}],
                                         params={
                                             "api-version": self.VERSION,
                                             "to": to_language,
                                             **from_dict,
                                             **alignment_dict,
                                         },
                                         headers={
                                             "Ocp-Apim-Subscription-Key": self.subscription_key,
                                             "Content-type": "application/json",
                                             "X-ClientTraceId": str(uuid.uuid4()),
                                             **self.region_headers
                                         },
                                         )
        response_json = response.json()
        self._logger.debug("%s got response: %s", self.VERSION, response_json)
        self.handle_api_error(response_json)

        detected_language_confidence = detected_language = None

        if from_language is None:
            try:
                detected_language = response_json[0]["detectedLanguage"]["language"]
                detected_language_confidence = response_json[0]["detectedLanguage"][
                    "confidence"
                ]
            except KeyError:
                raise DetectionError(
                    f"{self.name_ver} engine could not detect which language the source text is in"
                )

        try:
            translated_text = response_json[0]["translations"][0]["text"]
        except (KeyError, IndexError) as e:
            raise TranslationError(
                f"{self.name_ver} engine could not translate the given text"
            ) from e

        alignment = None
        if with_alignment:

            try:
                alignment_raw = response_json[0]["translations"][0]["alignment"]
            except KeyError:
                raise AlignmentError(
                    f"{self.name_ver} engine could not retrieve alignment information"
                )

            alignment = parse_alignment_string(alignment_raw["proj"])

        return TranslationResponse(
            engine=self.NAME,
            engine_version=self.VERSION,
            source_text=source_text,
            from_language=from_language or detected_language,
            to_language=to_language,
            detected_language_confidence=detected_language_confidence,
            translated_text=translated_text,
            alignment=alignment,
        )
