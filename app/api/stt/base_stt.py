from abc import ABC, abstractmethod

from app.utils.settings import available_stt_models, available_stt_languages


class BaseSpeechToText(ABC):
    def __init__(self, input_file: str, model: available_stt_models,
                 language: available_stt_languages):
        self.input_file = input_file
        self.model = model
        self.language = language


    @abstractmethod
    async def transcribe(self) -> str: ...

    @abstractmethod
    async def extract_audio_from_video(self) -> None: ...