import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = 'C!')

@client.event
async def on_ready():
  print('Bot is ready.')
  
#an example of a command would be
#@client.command()
#async def hello(ctx):
#   await ctx.send(f'Hello {ctx.author}')

client.run(os.getenv(TOKEN)
