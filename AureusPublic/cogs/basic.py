import discord
from discord.ext import commands
import pyjokes
from datetime import date, datetime
import time
import os
from dotenv import load_dotenv
load_dotenv()
MOD_ROLE = os.getenv('MOD_ROLE')


class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='echo', help='Echoes a message')
    @commands.is_owner()
    async def echo(self, ctx, *, echo):
        await ctx.send(echo)

    @commands.command(name='say', help='says')
    @commands.is_owner()
    async def say(self, ctx, *, say):
        await ctx.message.delete()
        await ctx.send(say)

    @commands.command(name='ping', help="Displays Aureus' latency")
    @commands.is_owner()
    async def ping(self, ctx):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()
        await message.delete()
        ping_embed = discord.Embed(title="<:ping_pong:809530048880181279> Pong!", color=discord.Color(0x00ffff))
        ping_embed.add_field(name="Websocket:", value=f"{round(self.bot.latency * 1000, 2)}ms", inline=True)
        ping_embed.add_field(name="API:", value=f"{round((end_time-start_time) * 1000, 2)}ms", inline=True)
        await ctx.send(embed=ping_embed)

    @commands.command(name='status', help="Changes Aureus' status")
    @commands.has_role(int(MOD_ROLE))
    async def status(self, ctx, *, status: str):
        await self.bot.change_presence(activity=discord.Game(name=f"{status}"))
        await ctx.message.delete()

    @commands.command(name='pfp', help='grabs pfps')
    @commands.cooldown(1, 25, commands.BucketType.channel)
    async def grab(self, ctx, member: discord.Member):
        await ctx.channel.send(member.avatar_url_as(static_format='png', size=2048))
# old one was ctx.author.avatar_url_as(format='png'))
# read here under "discord converters," super useful
# https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
# and https://discordpy.readthedocs.io/en/latest/api.html#discord-api-models for more

    @grab.error
    async def grab_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Calm down! You can't do this for {round(error.retry_after)} more seconds.", delete_after=3)

    @commands.command(name='joke', help='Tells a programming joke')
    async def joke(self, ctx):
        await ctx.send(pyjokes.get_joke())

    @commands.command(name='time', help="Displays current date and time from the host's machine")
    @commands.cooldown(1, 25, commands.BucketType.channel)
    async def time(self, ctx):
        await ctx.message.delete()
        at_time = datetime.now()
        current_time = at_time.strftime("%I:%M %p")
        today = date.today()
        today_date = today.strftime("%A, %b %Y")
        time_embed = discord.Embed(title="Need the time?", color=discord.Color(0x00ffff), timestamp=datetime.now())
        time_embed.set_footer(text=f"{ctx.author.name}", icon_url="https://mchcwi.org/wp-content/uploads/2020/07/123-1239314_alarm-clock-icons-clock-icon-clipart.jpg")
        time_embed.add_field(name="This is a test command. Who would need the time when on a device with internet? \nThe time right now is:", value=f"{current_time} ET")
        await ctx.channel.send(embed=time_embed)

    @time.error
    async def time_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Calm down! You can't do this for {round(error.retry_after)} more seconds.", delete_after=3)


def setup(bot):
    bot.add_cog(BasicCog(bot))
