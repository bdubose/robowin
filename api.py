"""Functions for interacting with the web."""

from io import BytesIO
from datetime import datetime
import os
import aiohttp
from PIL import Image

async def download_image(url: str) -> Image:
    """Fetches image from provided url"""
    async with aiohttp.request('GET', url) as response:
        return Image.open(BytesIO(await response.read()))

async def create_guild_event(
        guild_id: int,
        name: str,
        location:str,
        begin: datetime,
        end: datetime) -> int:
    """Creates an event in the provided guild"""
    body = {
        'name': name,
        'scheduled_start_time': begin.isoformat(),
        'scheduled_end_time': end.isoformat(),
        'entity_type': 3,
        'entity_metadata': {
            'location': location
        },
        'privacy_level': 2,
    }
    headers = {
        'Authorization': f'Bot {os.getenv("DISCORD_TOKEN")}'
    }
    url = f'https://discord.com/api/guilds/{guild_id}/scheduled-events'
    async with aiohttp.request('POST', url, json=body, headers=headers) as response:
        return response.status
