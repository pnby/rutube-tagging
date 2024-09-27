import logging

from fastapi import FastAPI

from app import setup_event_loop
from app.routes.tags import router as tag_router

logging.basicConfig(
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)

setup_event_loop()
app = FastAPI()
app.include_router(tag_router, prefix="/v1/api")
