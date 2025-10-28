import discord
from discord.ext import commands
from discord import app_commands
from ..utils.ticket_utils import create_ticket_channel, close_ticket_channel
from config import GUILD_ID


class TicketView(discord.ui.View):
def __init__(self):
super().__init__(timeout=None)


@discord.ui.button(label='Deschide un ticket', style=discord.ButtonStyle.primary, custom_id='open_ticket')
async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
await interaction.response.defer(ephemeral=True)
channel = await create_ticket_channel(interaction.guild, interaction.user, interaction.client)
await interaction.followup.send(f'Ticket creat: {channel.mention}', ephemeral=True)




class Tickets(commands.Cog):
def __init__(self, bot: commands.Bot):
self.bot = bot


@app_commands.command(name='setup_ticket', description='Postează mesajul pentru deschiderea ticketelor')
@app_commands.checks.has_permissions(manage_guild=True)
async def setup_ticket(self, interaction: discord.Interaction):
view = TicketView()
await interaction.channel.send('Apasă butonul pentru a crea un ticket.', view=view)
await interaction.response.send_message('Mesajul de setup a fost postat.', ephemeral=True)


async def setup(bot: commands.Bot):
guild = None
if GUILD_ID:
guild = discord.Object(id=GUILD_ID)
await bot.add_cog(Tickets(bot), guild=guild)
