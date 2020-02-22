import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
import os


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Ram Ranch', type = 2))
    print('Loading 74ip bot')


@client.event
async def on_message(message):
    if (' ') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
client.run(str(os.environ.get('BOT_TOKEN')))
