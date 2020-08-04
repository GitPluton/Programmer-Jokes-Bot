import discord
from discord.ext import commands
import pyjokes
import os

bot = commands.Bot(command_prefix = "Nothing")

@bot.event
async def on_message(msg):
  if msg.guild.me.mentioned_in(msg):
    await msg.channel.send(pyjokes.get_joke())
    
    
bot.run(os.environ['token'])
