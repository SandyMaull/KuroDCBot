from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import music

load_dotenv()

cogs = [music]
client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

@client.event
async def on_ready():
  print("{0.user} successful log in! ".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith('$hello'):
    await message.channel.send('Hello {user} ! \nHow r u today? \n'.format(user=message.author))
  await client.process_commands(message)

client.run(os.getenv('TOKEN'))