import discord
from discord.ext import commands
import typing

class slap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ", ".join(x.name for x in members)
        await ctx.send('{} just got slapped {}'.format(slapped, reason))
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(slap(bot))
