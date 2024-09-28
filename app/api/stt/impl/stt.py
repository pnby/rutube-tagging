import os
from typing import override, final

import whisper
from ffmpeg.asyncio import FFmpeg

from app import logger
from app.api.stt.base_stt import BaseSpeechToText
from app.utils.settings import available_stt_models, available_stt_languages


@final
class SpeechToText(BaseSpeechToText):
    def __init__(self, input_file: str, model: available_stt_models = "base", language: available_stt_languages = "ru"):
        self.wav_file = None
        self.__audio_extracted = False
        super().__init__(input_file, model, language)

    @override
    async def transcribe(self) -> str:
        if not self.__audio_extracted:
            await self.extract_audio_from_video()

        if self.wav_file is None:
            raise ValueError("wav_file is not set")

        model = whisper.load_model(self.model)

        result = model.transcribe(self.wav_file, language=self.language)

        return result['text']

    @override
    async def extract_audio_from_video(self) -> None:
        wav_file = os.path.splitext(self.input_file)[0] + '.wav'
        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(self.input_file)
            .output(
                wav_file,
                acodec="pcm_s16le",
                ar=16000
            )
        )
        await ffmpeg.execute()
        self.wav_file = wav_file
        self.__audio_extracted = True
