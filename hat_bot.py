from discord.ext import commands
import os
import discord  
import random

bot = discord.Client()
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='with my dick'))
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help Commands", description="List of commands that you can access from this bot.")
    embed.add_field(name="!ping", value="sends a pong bitch message", inline=False)
    embed.add_field(name="!say", value="literally repeats whatever argument you state", inline=False)
    embed.add_field(name="!roll", value="roll now to get mapotofu", inline=False)
    await ctx.channel.send(embed=embed)

bot.run('Mjc0OTYxOTAwMzY5MDg0NDE2.XfWqaw.I1lzpkwGuFVbQPFEcVZTi3nZZEk')