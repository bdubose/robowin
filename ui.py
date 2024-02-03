"""Ui for Discord bot"""

from discord import ButtonStyle, Interaction
from discord.ui import button, View, Button
from events import create_schedule_events

from schedule import Schedule

class ScheduleView(View):
    """Displays a Schedule with confirmation."""

    def __init__(self, schedule: Schedule):
        super().__init__()
        self.schedule = schedule

    @button(label="Add to Discord Calendar", style=ButtonStyle.primary, emoji="📅")
    async def add_to_calendar(self, interaction: Interaction, _: Button):
        """Allows user to add this schedule to the guild calendar."""
        await create_schedule_events(self.schedule, interaction.user, interaction.guild_id)
        await interaction.response.send_message('Added events.')
