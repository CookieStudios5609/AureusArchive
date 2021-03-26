from discord.ext import commands
from base64 import b64encode, b64decode


class Encode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='encode', help='Encodes a string in base64')
    async def encode(self, ctx, *, text: str):
        msg = b64encode(text.encode("utf-8"))
        await ctx.send("Done!")
        await ctx.message.delete()
        await ctx.send(msg.decode())

    @commands.command(name='decode', help='Decodes a string in base64')
    async def decode(self, ctx, *, text: str):
        msg = b64decode(text.encode())
        await ctx.send("Done!")
        await ctx.message.delete()
        await ctx.send(msg.decode())


def setup(bot):
    bot.add_cog(Encode(bot))
