import discord
from discord import app_commands
import os
import sqlite3
import tomllib
import re

#Load our config
with open('config.toml', 'rb') as fileObj:
    config = tomllib.load(fileObj) #dictionary/json

TOKEN = config["BOT_TOKEN"]
GUILD_ID = config["GUILD_ID"]
CHANNEL_ID = config["CHANNEL_ID"]

attachment_types = config["attachment_types"]



# +++++++++++ Client Setup +++++++++++ #
class EYE(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
eye = EYE(intents=intents)
# +++++++++++ Client Setup +++++++++++ #





def clear():
    os.system("clear||cls")


async def logger(message):
    userid = str(message.author.id)
    if message.attachments:
        media_msg = '(Media/attachment(s) uploaded.)'
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(media) for media in attachment_types):
                await attachment.save(f'attachments/{userid}_{attachment.filename}')
                print(f'Saved "{attachment.filename}" to directory "attachments"')
            else:
                pass
    else:
        media_msg = None

    media = media_msg
    author = str(message.author)
    content = str(message.content)
    time = str(message.created_at)
    guild = str(message.guild)
    channel = str(message.channel)
    row = [guild, channel, author, userid, time, content]
    conn = sqlite3.connect('chat_logs.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)", row)
    conn.commit()
    conn.close()

    if media:
        print(f"[{guild}] | [{channel}] | [@{author}] [{userid}] @ {time}: {media}")
    else:
        print(f"[{guild}] | [{channel}] | [@{author}] [{userid}] @ {time}: {content}")


@eye.event
async def on_ready():
    clear()
    print(f'Connection established, Logged in as {eye.user} (ID: {eye.user.id}')
    print('-----------')
    print("Reading chat...")


@eye.event
async def on_message(message):
    if message.author == eye.user: # Ignores itself
        return

    # logs specified channel in guild.
    if message.guild.id == GUILD_ID and message.channel.id == CHANNEL_ID:
        await logger(message)

    # logs messages in guild in all channels bot can see/read messages in.
    if message.guild.id == GUILD_ID and CHANNEL_ID == False:
        await logger(message)

    # All guilds the bot is in and in all channels that the bot can read message in.
    if GUILD_ID == False and CHANNEL_ID == False:
        await logger(message)
                

eye.run(TOKEN, reconnect=True)
