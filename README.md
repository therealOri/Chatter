# ChatterEye
Discord Chat logger. Log every message and attachment that gets sent on discord!
__ __

ChatterEye grabs chat messages & attachments from all servers your bot is in and from all of the channels it can see. You can also set it to only read from a server/guild of your choosing and a channel of your choosing in said guild. You can edit this in `config.toml`. Then it sends/Logs all chat messages into chat_logs.db, and saves attachments locally to '/attachments'.
The database is written in/for sqlite3, so you will need `DB Browser for SQLite` for viewing the databse.
__ __
🗒️ Note; <br> The links getting saved to the database when an attachment gets sent to chat will not work currently as discord implemented their new link system invalidating the links. And their new links will expire after 24hrs.
This feature of chatter may get removed unless I can think of a different way.

<br> 
<br>

# Installation
```
git clone https://therealOri/ChatterEye.git
cd ChatterEye
pip install -U discord.py
```
__ __

<br>
<br>

# Databse Viewer 
You can download it [Here](https://sqlitebrowser.org/).
#
![database_image](https://github.com/therealOri/Chatter/assets/45724082/6ccc1f3a-48ce-47f9-b332-e1eaf631295d.png)
__ __

<br>

# Notice
I am not responsible or liable on or off platform for the misuse or malicious purpose/applications of this code. Use at your own risk. If you get punished or banned, etc. for using this, that is ALL and FULLY on you. I made this code/project to be a proof of concept to show how easily you can log chat messages using discord bots/python code (pretty spooky right?). And I shall not be punished on discord/platform or off of discord/platform for making this code or for the actions of others/those who do decide to use this code in any way for any reason. This code is not intended to be used, you can or will get banned or get into deeper trouble.
