# Connects the bot to discord, hopefully
# if you're reading this, the test branch was made successfully! hooray!
import os
from datetime import datetime

import discord
import discord.ext
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('SERVER_NAME')
MOD_ROLE = os.getenv('MOD_ROLE')

intents = discord.Intents.default()
intents.members = True
prefix = "~"
bot = commands.Bot(command_prefix=prefix, intents=intents)
starter_cogs = ['cogs.basic', 'cogs.mod', 'cogs.listeners', 'cogs.Encode', 'cogs.MineServer', 'cogs.fun', 'cogs.music']
start_time = datetime.now()

bot.load_extension("jishaku")
# loads initial cogs
if __name__ == '__main__':
    for extension in starter_cogs:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == SERVER:
            break

    print(f'{bot.user} has successfully connected to {guild.name}!')
    channel = bot.get_channel(800842320135061504)
    await channel.send \
        (f"{bot.user} has connected to {guild.name} with a current ping of {round(bot.latency * 1000, 2)}ms. My command "
         f"prefix is: '{prefix}'.")
    song_name = 'against the odds!'  
    activity_type = discord.ActivityType.competing  
    await bot.change_presence(activity=discord.Activity(type=activity_type, name=song_name))


# cog commands. For the reloader, there is an overlap in a cog not loading and not existing. Revise it!
@bot.command(name='load', help='Loads cogs.')
@commands.has_role(int(MOD_ROLE))
async def load(ctx, cog_name: str):
    try:
        bot.load_extension('cogs.' + cog_name)
        await ctx.send(f"Loaded cogs.{cog_name} successfully.", delete_after=3)
    except commands.ExtensionAlreadyLoaded:
        await ctx.send(f'cogs.{cog_name} is already loaded!', delete_after=3)
    except commands.ExtensionNotFound:
        await ctx.send(f"cogs.{cog_name} doesn't exist!", delete_after=3)


# cog unloader
@bot.command(name='unload', help='Unloads cogs.')
@commands.has_role(int(MOD_ROLE))
async def unload(ctx, cog_name: str):
    try:
        bot.unload_extension('cogs.' + cog_name)
        await ctx.send(f"unloaded cogs.{cog_name} successfully.", delete_after=3)
    except commands.ExtensionNotLoaded:
        await ctx.send(f"cogs.{cog_name} isn't loaded!", delete_after=3)
    except commands.ExtensionNotFound:
        await ctx.send(f"cogs.{cog_name} doesn't exist!", delete_after=3)


# "Trying to get a new command in a new cog to work right" command
@bot.command(name='reload', help='Reloads cogs.')
@commands.has_role(int(MOD_ROLE))
async def reload(ctx, cog_name: str):
    try:
        bot.reload_extension('cogs.' + cog_name)
        await ctx.send(f"Reloaded cogs.{cog_name} successfully.", delete_after=3)
    except commands.ExtensionNotLoaded:
        await ctx.send(f"cogs.{cog_name} wasn't loaded!", delete_after=3)
    except commands.ExtensionNotFound:
        await ctx.send(f"cogs.{cog_name} doesn't exist!", delete_after=3)


# shutdown command
@bot.command(name='begone', help='Kills bot')
@commands.has_role(int(MOD_ROLE))
async def begone(ctx):
    await ctx.send("Guess I'll die... <:notlikethis:524783295343493120>")
    await ctx.bot.logout()


# currently doesn't work, should reply to role-related errors
# March 5 2021 update: I know how to fix this now
@begone.error
async def begone_error(ctx, error):
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You don't have the necessary role!")
        print('no role, nerd')


@bot.command()
async def uptime(ctx):
    buptime = datetime.now() - start_time
    hours, remainder = divmod(int(buptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"Aureus has been running for for: {days} days, {hours} hours, {minutes} min, {seconds}s")


bot.run(TOKEN)
