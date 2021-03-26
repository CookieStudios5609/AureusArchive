import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import random


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gray', help='work in progress')
    async def gray_test(self, ctx, member: discord.Member, caption):
        user_pfp = member.avatar_url_as(static_format='png', size=2048)
        await user_pfp.save('FunStuff/pfp.png')
        editable = Image.open('FunStuff/pfp.png')
        new_edit = editable.convert('L')
        width, height = new_edit.size
        draw = ImageDraw.Draw(new_edit)
        img_font = ImageFont.truetype("Plumpfull.ttf", size=40)
        draw.text((width / 2, 60), f"{caption}", fill='white', font=img_font, stroke_width=5, stroke_fill='red',
                  anchor='mm', align='center') # note that "white" or "black" work fine, but "red" returns black
        new_edit.save('FunStuff/Epfp.png')
        await ctx.channel.send(file=discord.File(r'FunStuff/Epfp.png'))

# removed rock paper scissors. Reimplement once postgre is learned and NewBot is ready


def setup(bot):
    bot.add_cog(FunCog(bot))
