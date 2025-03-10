import asyncio
import json
import os
import sys
import time
from discord import Intents, Client, Message
from discord.ext import commands
from dotenv import load_dotenv
from typing import Final

#Get discord token
env_path: str = 'venv/.env'
load_dotenv(env_path)
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Setup intents
intents: Intents = Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents) #what type of object would this be? :/

#JFF variables
with open('./data/banner.json', 'r') as file:
    data = json.load(file)
banner = data['banner']

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    await bot.tree.sync()
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print(f'Successfully logged in as {bot.user}')

async def main():
    await load_cogs()
    await bot.start(token=TOKEN)

asyncio.run(main())


