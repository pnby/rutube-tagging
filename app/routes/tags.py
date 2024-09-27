import os

from fastapi import APIRouter, HTTPException, File, UploadFile

from app import upload_directory
from app.utils.ffmpeg import convert_to_wav
from app.utils.settings import ALLOWED_VIDEO_TYPES

router = APIRouter()

@router.post("/tags/all/")
async def get_all_tags():
    return


@router.post("/tags/json/")
async def text_to_tags(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_VIDEO_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload the video.")


    file_location = os.path.join(upload_directory, file.filename)

    with open(file_location, "wb") as buffer:
        while chunk := await file.read(1024 * 1024):
            buffer.write(chunk)


    wav_file = os.path.splitext(file_location)[0] + '.wav'
    await convert_to_wav(file_location, wav_file)
