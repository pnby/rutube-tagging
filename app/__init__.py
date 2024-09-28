import logging
import os

import torch

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

cuda_available = torch.cuda.is_available()
torch.device("cuda" if cuda_available else "cpu")
if not cuda_available:
    logger.warning("Cuda cores are unavailable, switching to CPU")
upload_directory = make_base_dirs()
