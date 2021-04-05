import discord
import random
import os
from stay_alive import stay_alive

intents=intents=discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Connected')
  print(client.user)

@client.event
async def on_member_join(member):
 await member.create_dm()
 await member.dm_channel.send(
   f'Hi {member.name}, remember to stay civil in the chats. Remember, words can hurt more than actions! Words kill, words give life; they\'re either poison or fruit--- YOU choose.')

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    warning = ['Hmm... that is not a nice word.', 'Watch what you are saying please!', 'Remember, be nice!']
    negative = ['dumb', 'stupid', 'ugly', 'awful', 'atrocious', 'annoying','disgusting', 'failure','gross', 'filthy', 'hate','hideous', 'mentally-ill', 'unwanted', 'unwelcome', 'creep']
    if any(word in message.content for word in negative):
      await message.channel.send(random.choice(warning))

token = os.environ.get('discord_top_secret')
client.run(token)

stay_alive()

