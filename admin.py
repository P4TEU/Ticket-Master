import discord
from discord.ext import commands
from discord import app_commands


class Admin(commands.Cog):
def __init__(self, bot: commands.Bot):
self.bot = bot


@app_commands.command(name='forceclose', description='Închide ticketul curent (doar staff)')
@app_commands.checks.has_permissions(manage_guild=True)
async def forceclose(self, interaction: discord.Interaction):
channel = interaction.channel
await interaction.response.defer(ephemeral=True)
await channel.delete(reason='Ticket închis forțat de staff')
await interaction.followup.send('Ticket închis.', ephemeral=True)


async def setup(bot: commands.Bot):
await bot.add_cog(Admin(bot))
