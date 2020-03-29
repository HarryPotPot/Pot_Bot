import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(jdata['Channel'])
        await channel.send(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(jdata['Channel'])
        await channel.send(f'{member} left!')    

    @commands.Cog.listener()
    async def on_message(self, msg):
        keywords = ['apple', 'pen']
        for keyword in keywords:
            if keyword in msg.content and msg.author != self.bot.user:
                await msg.channel.send('apple')
                break

def setup(bot):
    bot.add_cog(Event(bot))