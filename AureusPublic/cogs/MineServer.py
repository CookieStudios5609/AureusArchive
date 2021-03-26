import discord
from discord.ext import commands
import mcstatus as m
import datetime


class MineServerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mci', help='Gets info for a Minecraft server.')
    async def mci(self, ctx, ip: str = None):
        s = m.MinecraftServer(ip)
        ping = s.ping()
        status = s.status()
        pcount = status.players.online
        maxpcount = status.players.max
        ver = status.version.name
        motd = status.description['text']  
        embed = discord.Embed(title=f'{motd}', color=discord.Color(0x00ffff), timestamp=datetime.datetime.now())
        embed.add_field(name=f"Info for {ip}: ", value=f"Version: {ver}")
        embed.add_field(name=f"This server is currently online.", value=f"{pcount} of {maxpcount} players are ingame.", inline=False)
        embed.set_footer(text=f"{ping}ms")
        await ctx.channel.send(embed=embed)

# TODO: Find a way to make this embed ignore info not provided by the server. Some servers don't send ping. Some don't send a MOTD. Some don't send playercount.
# There must be a way without making a new command for EVERY case. Find out how!
    @commands.command(name='mci2', help='Gets info for a Minecraft server WITHOUT getting the ping.')
    async def mci2(self, ctx, ip: str = None):
        s = m.MinecraftServer(ip)
        # ping = s.ping()
        status = s.status()
        print(status.raw)
        pcount = status.players.online
        maxpcount = status.players.max
        ver = status.version.name
        motd = status.description[0]  
        embed = discord.Embed(title=f'{motd}', color=discord.Color(0x00ffff), timestamp=datetime.datetime.now())
        embed.add_field(name=f"Info for {ip}: ", value=f"{ver}:")
        embed.add_field(name=f"This server is currently online.", value=f"{pcount} of {maxpcount} players are ingame.", inline=False)
        # embed.set_footer(text=f"{ping}ms")
        await ctx.channel.send(embed=embed)

    @mci.error
    async def mci_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Timed out. The server may be offline, or the bot host is having internet issues. Try the `mci2` command.", color=discord.Color(0x00ffff))
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MineServerCog(bot))
