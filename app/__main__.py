import logging

from fastapi import FastAPI

from app.routes.tags import router as tag_router

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)

app = FastAPI()
app.include_router(tag_router, prefix="/v1/api")
