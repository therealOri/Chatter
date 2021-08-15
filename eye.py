import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import os
import io
from rich.console import Console
from dotenv import load_dotenv
import sqlite3

load_dotenv()
TOKEN = os.getenv("TOKEN")


BOT_Prefix=("&.")
client = commands.Bot(command_prefix=BOT_Prefix, self_bot=True)
client.remove_command("help")


os.system('clear||cls')
BANNER = '''[magenta]
  ____ _           _   _            _____           
 / ___| |__   __ _| |_| |_ ___ _ __| ____|   _  ___ 
| |   | '_ \ / _` | __| __/ _ \ '__|  _|| | | |/ _ \
| |___| | | | (_| | |_| ||  __/ |  | |__| |_| |  __/
 \____|_| |_|\__,_|\__|\__\___|_|  |_____\__, |\___|
                                         |___/      

[green]by https://github.com/therealOri[/green]
[/magenta]
'''
console = Console()
console.print(BANNER)
print(Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established!, Reading chat...")



class MyClient(discord.Client):

    async def on_message(self, message):
      if message.author == self.user:
            return
      author = str(message.author)
      content = str(message.content)
      userid = str(message.author.id)
      time = str(message.created_at)
      guild = str(message.guild)
      channel = str(message.channel)
      row = [guild, channel, author, userid, time, content]

      conn = sqlite3.connect('chat_logs.db')
      c = conn.cursor()
      c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)", row) # Insert data

      # Save (commit) the changes then close the file.
      conn.commit()
      conn.close()

      print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]" + Fore.LIGHTRED_EX + "[{}] | [{}] | [{}] [{}] @ {}: {}".format(guild, channel, author, userid, time, content))

client = MyClient()
client.run(TOKEN)