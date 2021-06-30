from keep_alive import keep_alive
import discord
import os

client = discord.Client()
@client.event
async def on_ready():
    print("bot is online")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers, type /help CursedBot.inc Copyright 2021"))
    await client.get_channel(806946593758).send("bot is hosting")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content
  if msg.startswith("hi"):
    await client.get_channel.send("Hi there")
  

keep_alive()
my_secret = os.environ['TOKEN']
client.run (my_secret)
