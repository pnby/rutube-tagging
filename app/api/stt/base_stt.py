from abc import ABC, abstractmethod

from app.utils.settings import available_stt_models, available_stt_languages


class BaseSpeechToText(ABC):
    def __init__(self, input_file: str, model: available_stt_models,
                 language: available_stt_languages):
        """
        Initialize the BaseSpeechToText class.

        :param input_file: Path to the input file (audio or video).
        :param model: The speech-to-text model to use.
        :param language: The language of the audio.
        """
        self.input_file = input_file
        self.model = model
        self.language = language

    @abstractmethod
    async def transcribe(self) -> str:
        """
        Transcribe the audio content from the input file.

        :return: Transcribed text as a string.
        """


    @abstractmethod
    async def extract_audio_from_video(self) -> None:
        """
        Extract audio from the input video file.

        :return: None
        """
