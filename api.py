"""Functions for interacting with the web."""

from io import BytesIO
import requests
from PIL import Image


def download_image(url: str) -> Image:
    """Fetches image from provided url"""
    response = requests.get(url, timeout=15)
    return Image.open(BytesIO(response.content))
