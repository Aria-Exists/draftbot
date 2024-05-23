

import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

with open('projects/draftbot/key.txt') as f:
    BOTKEY = f.readline().strip('\n')

client.run(BOTKEY)
