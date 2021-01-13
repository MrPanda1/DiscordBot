import discord
import os
from dotenv import load_dotenv

# Load vars from .env file into environment variables
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # If I wrote the message, do nothing
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
client.run(os.getenv('TOKEN'))