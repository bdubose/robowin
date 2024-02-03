"""Functions for create Discord guild events, currently the Discord API client
does not implement this functionality, so we must do it ourselves."""

import os
from typing import Union
from discord import Member, User
from api import create_guild_event
from schedule import Schedule

token = os.getenv('DISCORD_TOKEN')

async def create_schedule_events(schedule: Schedule, user: Union[User, Member], guild_id: int):
    """Creates events for all days scheduled."""
    scheduled_days = (day for day in schedule.days if day.begin is not None)
    for day in scheduled_days:
        await create_guild_event(
            guild_id,
            f'{user.display_name} Working',
            'Publix',
            day.begin,
            day.end)
