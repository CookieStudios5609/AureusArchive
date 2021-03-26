import random

from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        friend_response = [
            'only plays busted characters',
            'rarely plays MK11.',
            '12149',
            'WACK'
        ]

        if message.author == self.bot.user:
            return
        if 'yah' in message.content:
            await message.channel.send('nah')
        if message.content == "a friend's name":
            friend_msg = random.choice(friend_response)
            await message.channel.send(friend_msg)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print('someonejoinedorsomething')
        channel = self.bot.get_channel(800842320135061504)
        await channel.send(f'Welcome {member}')

# joke
    '''@commands.Cog.listener()
    async def on_member_join(self, member):
        if member.id == 159985870458322944:
            await member.kick(reason="Mee6 is not allowed here!")'''


def setup(bot):
    bot.add_cog(Listeners(bot))
