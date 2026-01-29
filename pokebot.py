import discord
import requests
import json
import random

def getPoke():
  rng_pokemon = random.randint(1, 1025)
  if (random.randint(1,100) == 33):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{rng_pokemon}.png"
  else:
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{rng_pokemon}.png"

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return 
    if message.content.startswith('$pokemon'):
      await message.channel.send(getPoke())  

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('') # put discord token here
