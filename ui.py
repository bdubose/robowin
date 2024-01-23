"""Ui for Discord bot"""

from discord import ButtonStyle, Interaction
from discord.ui import button, View, Button

class ScheduleView(View):
    """Displays a Schedule with confirmation."""

    @button(label="Add to Google Calendar", style=ButtonStyle.primary, emoji="📅")
    async def add_to_calendar(self, interaction: Interaction, button: Button):
        """Allows user to add this schedule to their calendar."""
        await interaction.response.send_message('Coming soon!', ephemeral=True)
