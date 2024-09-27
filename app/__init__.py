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


def setup_event_loop():
    try:
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            try:
                import uvloop # noqa
            except ImportError:
                logger.info("Installing uvloop...")
                subprocess.run([sys.executable, "-m", "pip", "install", "uvloop"], check=True)
                import uvloop # noqa

            uvloop.install()

            if hasattr(asyncio, 'get_child_watcher'):
                child_watcher = asyncio.SafeChildWatcher()
                asyncio.set_child_watcher(child_watcher)
                child_watcher.attach_loop(asyncio.get_event_loop())

            logger.info("uvloop has been successfully installed and configured.")
        elif sys.platform.startswith("win"):
            loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(loop)
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            logger.info("ProactorEventLoop installed")
    except subprocess.CalledProcessError as e:
        logger.warning(f"Error installing the 'uvloop' package: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during uvloop setup: {e}")

upload_directory = make_base_dirs()
