import discord
from discord.ext import commands
import time

class AboutCog(commands.Cog, name="about command"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "about",
                    usage="",
                    description = "Display the about page.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def about(self, ctx):
        message = await ctx.send("Hello! This is a bot that specializes in politics and breaking news! ---@clayton_sec---!")
        await message.edit(content=f"Hello! This is a bot that specializes in politics and breaking news! --- @clayton_sec---'")

def setup(bot:commands.Bot):
    bot.add_cog(AboutCog(bot))