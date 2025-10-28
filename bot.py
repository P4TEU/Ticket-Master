import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from config import TOKEN


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True


bot = commands.Bot(command_prefix='!', intents=intents)


# load cogs
for filename in os.listdir('./src/cogs'):
if filename.endswith('.py'):
bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
print(f'Logged in as {bot.user} (ID: {bot.user.id})')


bot.run(TOKEN)
