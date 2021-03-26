import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
MOD_ROLE = os.getenv('MOD_ROLE')


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# blocks EVERY word in filter.txt. Change this if this bot ends up in a large enough server
    with open('assets\\filter.txt', 'r') as f:
        global black_list
        blocked_words = f.read()
        black_list = blocked_words.split()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        for blocked_words in black_list:
            if blocked_words in message.content:
                await message.delete()
                await message.channel.send(f"Don't say that {message.author.mention}!")

    @commands.command(name='purge', help='Mass deletes messages')
    @commands.has_role(int(MOD_ROLE))
    async def purge(self, message, purge_num: int):
        await message.channel.purge(limit=purge_num + 1)
        await message.channel.send(f"{purge_num} messages and purge command request cleared "
                                   f"by {message.author.mention}!")

    @commands.command(name='ban', help='Destroys naughty users')
    @commands.has_role(int(MOD_ROLE))
    async def ban(self, ctx, user: discord.User, ban_reason=None):
        if user is None or user is ctx.message.author:
            await ctx.channel.sent("can't ban yourself, nerd")
            return
        if ban_reason is None:
            ban_reason = "Moderator discretion"
            print('hi')
        ban_message = f"You have been banned from {ctx.guild.name} for `{ban_reason}`"
        await user.send(ban_message)
        await ctx.guild.ban(user, reason=ban_reason)
        await ctx.channel.send(f"{user} has successfully been banned!")

# do I need this?
    @commands.command(name='fban', help="Destroys naughty users even if not in the server!")
    @commands.has_role(int(MOD_ROLE))
    async def ban(self, ctx, user: discord.User, ban_reason=None):
        if user is None or user is ctx.message.author:
            await ctx.channel.sent("can't ban yourself, nerd")
            return
        if ban_reason is None:
            ban_reason = "Moderator discretion"
        await ctx.guild.ban(user, reason=ban_reason)
        await ctx.channel.send(f"{user} has successfully been banned for {ban_reason}!")

# unban/funban is bad. You can't DM most users without being their friend or being in a guild with them.
# this bot would be neither, why did I waste time copying over "unban" to make "funban" if I knew unban wouldn't work?
    @commands.command(name='unban', help='Undestroys naughty users')
    @commands.has_role(int(MOD_ROLE))
    async def unban(self, ctx, user: discord.User, unban_reason=None):
        if unban_reason is None:
            unban_reason = "Moderator discretion"
        unban_message = f"You have been unbanned."
        await user.send(unban_message)
        await ctx.guild.unban(user)
        await ctx.channel.send(f"{user} has successfully been unbanned for {unban_reason}!")

    @commands.command(name='funban', help='Undestroys naughty users even if not in the server!')
    @commands.has_role(int(MOD_ROLE))
    async def unban(self, ctx, user: discord.User, unban_reason=None):
        if unban_reason is None:
            unban_reason = "Moderator discretion"
        await ctx.guild.unban(user)
        await ctx.channel.send(f"{user} has successfully been unbanned for {unban_reason}!")

# in progress, logs or does something with deleted messages, maybe dyno-like embed?
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.deleted = message

    @commands.command(name='holup')
    @commands.has_role(int(MOD_ROLE))
    async def holup(self, ctx):
        message = self.deleted.content
        embed = discord.Embed(title=f'HOLUP! Deleted message from {self.deleted.author}', description=message, color=discord.Color(0x00ffff), timestamp=datetime.datetime.now())
        embed.set_footer(text='Retrieved:')
        await ctx.send(embed=embed)

    @holup.error
    async def holup_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("There are no messages to retrieve!")

# todo: try this someday, put message.content as the text somehow and funnel it all into https://github.com/IBM/MAX-Toxic-Comment-Classifier or similar


def setup(bot):
    bot.add_cog(Mod(bot))
