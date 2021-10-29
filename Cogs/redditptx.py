import discord
from discord.ext import commands
import time
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
hot_posts = reddit.subreddit('politics').hot(limit=10)

class redditptx(commands.Cog, name="reddit politics news"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "redditptx",
                    usage="",
                    description = "Shows the top ten posts on /r/politics.")
    #Function that will post the top 10 posts from /r/politics
    @commands.cooldown(1, 0, commands.BucketType.member)
    async def redditptx(self, ctx):
        for post in hot_posts:
            message = await ctx.send(post.title)
            await message.edit(content=f" • " + post.title)
            


def setup(bot:commands.Bot):
    bot.add_cog(redditptx(bot))