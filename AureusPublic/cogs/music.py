import discord
from discord.ext import commands
import nacl


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        ''' everything about this cog was a struggle, and it still can only play one audio file. YTDL needs to be here someday'''

    @commands.command(name='MX')
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if ctx.voice_client is not None:
            await voice.disconnect()
        else:
            await ctx.send("Aureus is not connected to a voice channel right now.")

    @commands.command(name='play', help='joins a music channel')
    async def join(self, ctx, channel: commands.VoiceChannelConverter = None):
        # voicechannelconverter and these if statements are used to let you type the command for a specific channel to
        # join, OR type with no arguments to join the person who invoked the command. Why do some bots not have this? There must be a flaw I'm missing...
        if channel is None:
            channel = ctx.message.author.voice.channel
        else:
            channel = channel
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        song = 'dumb.mp3'
        source = discord.FFmpegPCMAudio(song)
        embed = discord.Embed(title=f'<:musical_note:814236611045752862> Now Playing: {song} <:musical_note:814236611045752862>', color=discord.Color(0x00ffff))
        await ctx.channel.send(embed=embed)
        voice.play(source)

    @commands.command(name='pause')
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send('Nothing is playing')

    @commands.command(name='resume')
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.resume()


def setup(bot):
    bot.add_cog(Music(bot))


'''  # leave channel
    @commands.command(name='MX')
    async def leave(self, ctx, channel: commands.VoiceChannelConverter):
        await channel.disconnect()'''
