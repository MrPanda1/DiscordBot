import discord
from dotenv import load_dotenv
import json
import os

# Load vars from .env file into environment variables
load_dotenv()

# Get config vars
config = json.load(open('config.json', 'r'))

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(config)

@client.event
async def on_message(message):
    # Make sure we have the proper prefix
    if not message.content.startswith(config['prefix']):
        return

    # If the bot wrote the message, do nothing
    if message.author == client.user:
        return

    # Get command and args for cmd here
    try:
        cmd, args = message.content[len(config['prefix']) : len(message.content)].split(None, 1)
    except ValueError:
        cmd = message.content[len(config['prefix']) : len(message.content)]
        args = None

    if cmd.lower() == 'ping':
        await message.channel.send('Pong')
    elif cmd.lower() == 'echo':
        await message.channel.send(f'Echoing: {args}')
    
client.run(os.getenv('TOKEN'))