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
   if message.content == '-ramranch':
        em = discord.Embed(description='ramranch')
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=MADvxFXWvwE')
        await client.send_message(message.channel, embed=em)
   if message.content == '-jayboss980isafreakingod':
        em = discord.Embed(description='CRABRAVE')
        em.set_image(url='https://media.giphy.com/media/S46AgOqU95FHa/giphy.gif')
        await client.send_message(message.channel, embed=em)
   if message.content.startswith('-8ball'):
        randomlist = ['Maybe','Yes','No',]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run(str(os.environ.get('BOT_TOKEN')))
