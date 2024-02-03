"""Functions for interacting with the web."""

from io import BytesIO
import aiohttp
from PIL import Image

async def download_image(url: str) -> Image:
    """Fetches image from provided url"""
    async with aiohttp.request('GET', url) as response:
        return Image.open(BytesIO(await response.read()))
