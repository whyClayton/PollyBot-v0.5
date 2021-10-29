import discord
from discord.ext import commands
import time
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
hot_posts = reddit.subreddit('energy').hot(limit=10)

class energynews(commands.Cog, name="reddit economicnews news"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "energynews",
                    usage="",
                    description = "Shows the top ten posts on /r/energy")
    #Function that will post the top 10 posts from /r/energy
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def energynews(self, ctx):
        for post in hot_posts:
            message = await ctx.send(post.title)
            await message.edit(content=f" • " + post.title)
            print("worked.")

def setup(bot:commands.Bot):
    bot.add_cog(energynews(bot))