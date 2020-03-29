import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = '/')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def picture(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)


bot.run(jdata['TOKEN'])