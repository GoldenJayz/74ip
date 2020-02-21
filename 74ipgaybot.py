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
   if message.content == '-creator':
        await client.send_message(message.channel,'@Jaden#3147')
   if message.content == '-meme':
        randomlist = ['https://i.ytimg.com/vi/Unxy0tPrxjg/maxresdefault.jpg','Yes','No',]
   if ('penis') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('shit') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('nigger') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('nigga') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('fuck') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('bitch') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('prick') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('bastard') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('ass') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if ('asshole') in message.content:
        await client.delete_message(message)    
        await client.send_message(message.channel,'Do not swear! Mods/Admins have been alerted! <@%s>'  %(message.author.id))
   if message.content == ('-74ip'):
        if message.author.id == "641772453168676886":
            await client.send_message(message.channel,'Hi queen 74ip how may I serve you?')
        else:
            await client.send_message(message.channel, "Only the owner of this bot can access this command. Sorry!")
client.run(str(os.environ.get('BOT_TOKEN')))
