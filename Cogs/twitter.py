import discord
from discord.ext import commands
import time


class TwitterCog(commands.Cog, name="twitter command"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "devtwitter",
                    usage="",
                    description = "Shows the Dev's(me) twitter page.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def twitter(self, ctx):
        message = await ctx.send("https://twitter.com/clayton_sec")
        await message.edit(content=f"https://twitter.com/clayton_sec")

def setup(bot:commands.Bot):
    bot.add_cog(TwitterCog(bot))