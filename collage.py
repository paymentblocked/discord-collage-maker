from urllib.parse import urlparse
import discord
from discord import Embed
from discord.ext import commands
from os import system
import subprocess
import requests
import json
import checks

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  
    activity = discord.Activity(name="...", type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Status.dnd, activity=activity)


@client.event
async def on_message(message):

    botSpam = client.get_channel(spamChannelID)
    gains = client.get_channel(successID)
    if botSpam.id == message.channel.id:
        if message.content.startswith(".getSuccess"):
            userContent = message.content
            newContent = userContent.split(" ")
            num = int(newContent[1])+1
            messages = [m async for m in gains.history(limit=num)]
            pictures = []
            for m in messages:
                if m.attachments == []:
                    pass
                else:
                    pictures.append(m.attachments)

            linkArray = checks.runPictures(pictures)
            checks.requestPics(linkArray)
            checks.checkDupes()
            system("python collagerMaker.py")
            await botSpam.send(file=discord.File("output.png"))


    


client.run('token')
