import discord
from discord.ext import commands
import random
import typing

class _8ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
            "sure",
            "sure i guess",
            "uh huh sure",
            "ya of course",
            "yes do not worry about it",
            "yep ur totally right",
            "plausible",
            "uhhhhhhhhh sure",
            "ye",
            "YE ES maybe i dont know",
            "uhhh idk ask again",
            "idk i dont feel like responding, ask again later",
            "eh not gonna tell you bud",
            "idk cant tell",
            "try to be more clear cuz i dont understand what ur saying",
            "ehhhhhh nah",
            "my answer is no bud",
            "the owner of this bot made me say no",
            "mmmmm nope",
            "haha lol nope"
        ]
        embed = discord.Embed(title="8ball Question", description="", color=0x10e389)
        embed.add_field(name=f'{question}', value=f'{random.choice(responses)}', inline=False)
        embed.set_thumbnail(url='https://www.transparentpng.com/thumb/8-ball-pool/yGrfOj-8-ball-pool-wonderful-picture-images.png')
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(_8ball(bot))
