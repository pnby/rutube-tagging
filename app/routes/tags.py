import json
import os

from fastapi import APIRouter, HTTPException, File, UploadFile

from app import upload_directory, logger
from app.api.llama.impl.llama import Llama
from app.api.stt.impl.stt import SpeechToText
from app.utils.prompt import Prompt
from app.utils.settings import ALLOWED_VIDEO_TYPES

router = APIRouter()

@router.post("/tags/all/", summary="Get all tags", description="Endpoint to retrieve all tags.")
async def get_all_tags():
    """
    Retrieves all tags.

    Returns:
        dict: A dictionary containing all tags.
    """
    return

@router.post("/tags/media/", summary="Extract tags from media file", description="Endpoint to extract tags from a media file.")
async def text_to_tags(file: UploadFile = File(...)):
    """
    Extracts tags from a media file.

    Args:
        file (UploadFile): The media file to be processed.

    Returns:
        dict: A dictionary containing the extracted tags.

    Raises:
        HTTPException: If the file format is invalid.
    """
    if file.content_type not in ALLOWED_VIDEO_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload the video.")


    file_location = os.path.join(upload_directory, file.filename)

    with open(file_location, "wb") as buffer:
        while chunk := await file.read(1024 * 1024 * 10):
            buffer.write(chunk)


    stt = SpeechToText(input_file=file_location)
    text = await stt.transcribe()

    prompt = Prompt(text)
    logger.debug(f"\nSYSTEM PROMPT: {prompt.get_system_prompt()}\nUSER PROMPT: {prompt.get_user_prompt()}")

    llama = Llama(prompt.get_user_prompt(), system_prompt=prompt.get_system_prompt())
    await llama.send_request()

    formatted_response = llama.get_formatted_response().replace("'", '"')
    try:
        formatted_response = json.loads(formatted_response)
    except Exception as e:
        logger.warning(f"The LLM response could not be converted to json\n{e}\n{formatted_response}")
    return formatted_response

