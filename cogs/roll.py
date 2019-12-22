import discord
from discord.ext import commands

class roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx):
        embed = discord.Embed(title="Summoning Results:", description="", color=0x00ff00)
        embed.set_image(url='https://i.imgur.com/OSY5wgz.png')
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(roll(bot))