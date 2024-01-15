import discord
from discord import app_commands
import os
import sqlite3
import tomllib

#Load our config
with open('config.toml', 'rb') as fileObj:
    config = tomllib.load(fileObj) #dictionary/json

TOKEN = config["BOT_TOKEN"]
GUILD_ID = config["GUILD_ID"]
CHANNEL_ID = config["CHANNEL_ID"]



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


def logger(message):
    author = str(message.author)
    content = str(message.content)
    userid = str(message.author.id)
    time = str(message.created_at)
    guild = str(message.guild)
    channel = str(message.channel)
    row = [guild, channel, author, userid, time, content]
    conn = sqlite3.connect('chat_logs.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)", row)
    conn.commit()
    conn.close()
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
        logger(message)

    # logs messages in guild in all channels bot can see/read messages in.
    if message.guild.id == GUILD_ID and CHANNEL_ID == False:
        logger(message)

    # All guilds the bot is in and in all channels that the bot can read message in.
    if GUILD_ID == False and CHANNEL_ID == False:
        logger(message)
                

eye.run(TOKEN, reconnect=True)
