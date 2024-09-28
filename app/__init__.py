import asyncio
import logging
import os
import subprocess
import sys

logger = logging.getLogger(__name__)

def make_base_dirs() -> str:
    """
    Creates directories where the content will be downloaded
    :return:
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    upload_dir = os.path.join(parent_dir, 'uploads')

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    return upload_dir

upload_directory = make_base_dirs()
