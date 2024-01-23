"""Entry points for Discord bot commands."""

import os
import discord
from discord.ext import commands

from api import download_image
from otr import read_image_text
from schedule import Schedule
from ui import ScheduleView

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.last_texts = []

@bot.command()
async def echo(context: commands.Context, *, message:str):
    """Echoes back argument to Discord message"""
    await context.send(message)

@bot.command()
async def debug(context: commands.Context):
    """Prints all the last text read from the last images."""
    await context.send('Last images processed:')
    for text in bot.last_texts:
        await context.send(text)

@bot.command()
async def read_schedule(context: commands.Context):
    """Reads image attachments into Schedules."""
    bot.last_texts = []
    image_urls = context.message.attachments
    count = len(image_urls)
    if count == 0:
        await context.send('No images found 😔')
        return

    await context.send(f'Processing {count} image{"" if count == 1 else "s"}...')
    for image_url in image_urls:
        image = download_image(image_url)
        text = read_image_text(image)
        bot.last_texts.append(text)
        schedule = Schedule(text)
        await context.send(str(schedule), view=ScheduleView() if schedule.error is None else None)

bot.run(os.getenv('DISCORD_TOKEN'))
