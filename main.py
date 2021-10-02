import discord
import os

import random

client = discord.Client()

dacey_words = ["dacey", "dack", "decay", "dog doin", "dacky", "dace", "dacku"]

dacey_urls = [
  "https://imgur.com/a/WCxXe6Z",
  "https://imgur.com/a/E1bfPt1",
  "https://imgur.com/u67JIEj",
  "https://imgur.com/a/HUTzbyZ",
  "https://imgur.com/IaU2j9e",
  "https://imgur.com/a/b4BrQh6",
  "https://imgur.com/a/YGQfLJF",
  "https://imgur.com/a/ECf0F3W",
  "https://imgur.com/a/FaqPoQD",
  "https://imgur.com/a/Pi2SNLq",
  "https://imgur.com/a/vKsS1vG",
  "https://imgur.com/a/M0R1INQ",
  "https://imgur.com/a/0OnDw3V",
  "https://imgur.com/a/EPaYlDP",
  "https://imgur.com/iytu89N",
  "https://imgur.com/a/KJImRKD",
  "https://imgur.com/a/VcKRMGD",
  "https://imgur.com/a/tqr9GQT",
  "https://imgur.com/a/RdMQd9c",
  "https://imgur.com/a/ECcUaR5",
  "https://imgur.com/a/d6Fbwhx",
  "https://imgur.com/a/RrjgyPB",
  "https://imgur.com/a/55A6iQr",
  "https://imgur.com/a/pEgZesC",
  "https://imgur.com/a/OgSkXyp",
  "https://imgur.com/a/wLtJQt9",
  "https://imgur.com/a/oLJX7rG",
  "https://imgur.com/a/qRkshkz",
  "https://imgur.com/a/MZ3faus",
  "https://imgur.com/a/LLukG7C",
  "https://imgur.com/a/Ym59yBU",
  "https://imgur.com/a/RyJM5zM",
  "https://imgur.com/a/sSKabTX",
  "https://imgur.com/a/i8hRcaq",
  "https://imgur.com/a/WZgwoAL",
  "https://imgur.com/a/pYEHR6y",
  "https://imgur.com/a/6yS0yYy",
  "https://imgur.com/a/YWwTY9O",
  "https://imgur.com/a/jxTAPaw",
  "https://imgur.com/a/rslsQLa",
  "https://imgur.com/a/Rd75ELh",
  "https://imgur.com/a/RaoTGAY",
  "https://imgur.com/a/iZ0048c",
  "https://imgur.com/a/r5Zoy75",
  "https://imgur.com/a/dXsTuiu",
  "https://imgur.com/a/k0FuSrH",
  "https://imgur.com/a/cAJmYTE",
  "https://imgur.com/a/cAJmYTE",
  "https://imgur.com/HlccRQT",
  "https://imgur.com/a/debMISV",
  "https://imgur.com/a/ihMhpvg",
  "https://imgur.com/a/geSJaNg",
  "https://imgur.com/a/V7wbFN6",
  "https://imgur.com/a/UPQXHQ6",
  "https://imgur.com/a/a8Ivz8K",
  "https://imgur.com/a/I5e9x8W",
  "https://imgur.com/a/y8QoeNs",
  "https://imgur.com/a/J0BtMeA",
  "https://imgur.com/a/0i65uRk",
  "https://imgur.com/a/Gis04k1",
  "https://imgur.com/a/ih72He4",
  "https://imgur.com/a/C4A7GSW",
  "https://imgur.com/a/ZgGrDHL",
  "https://imgur.com/a/qr3z6HJ",
  "https://imgur.com/a/JRwYlOk",
  "https://imgur.com/a/ZnjNwtc",
  "https://imgur.com/a/ocPJjbE",
  "https://imgur.com/a/B4yyejU",
  "https://imgur.com/a/12hyHUB",
  "https://imgur.com/a/BKRjPTb",
  "https://imgur.com/a/cPdbJgi",
  "https://imgur.com/a/aefohot",
  "https://imgur.com/a/Ij8lF2m",
  "https://imgur.com/a/BDdtRB4",
  "https://imgur.com/a/rnTLnq4",
  "https://imgur.com/a/axtmKLl",
  "https://imgur.com/a/t8j66sP",
  "https://imgur.com/a/DMEI3m5",
  "https://imgur.com/a/Y0jdZXY"
]



@client.event

async def on_ready():

  print('We have logged in as {0.user}'
  .format(client))

@client.event

async def on_message(message):

  if message.author == client.user:
    return

  msg = message.content.lower()

  if message.content.startswith('$test'):
    await message.channel.send("https://cdn.discordapp.com/attachments/792662367334301747/887583134202343444/image0.jpg")

  if message.content.startswith('$dacey'):
    await message.channel.send(random.choice(dacey_urls))
    


  elif any(word in msg for word in dacey_words):
    await message.channel.send(random.choice(dacey_urls))


my_secret = os.environ['TOKEN']
client.run(my_secret)
