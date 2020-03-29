import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def picture(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, times:int):
        await ctx.channel.purge(limit=times + 1)

def setup(bot):
    bot.add_cog(React(bot))