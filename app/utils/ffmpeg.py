from ffmpeg.asyncio import FFmpeg


async def convert_to_wav(input_file: str, output_file: str):
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(input_file)
        .output(
            output_file,
            acodec="pcm_s16le",
            ar=16000
        )
    )
    await ffmpeg.execute()