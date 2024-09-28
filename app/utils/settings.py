import os

from typing_extensions import Literal

# a constant that stores some data
available_llm_models: Literal["mistral"] = "mistral"
available_stt_models: Literal["base", "small"] = "small"
available_stt_languages: Literal["ru"] = "ru"
ALLOWED_VIDEO_TYPES = ["video/mp4", "video/x-matroska", "video/avi", "video/webm"]

MODE: Literal["DEV", "PROD"] = os.environ.get("__mode", "DEV")