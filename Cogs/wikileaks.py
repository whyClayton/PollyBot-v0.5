import discord
from discord.ext import commands
import time
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
hot_posts = reddit.subreddit('WikiLeaks').hot(limit=10)

class WikiLeaks(commands.Cog, name="reddit law news"):
    def __init__(self, bot:commands.Bot): 
        self.bot = bot

    @commands.command(name = "WikiLeaks",
                    usage="",
                    description = "Shows the top ten posts on /r/WikiLeaks.")
    #Function that will post the top 10 posts from /r/WikiLeaks
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def WikiLeaks(self, ctx):
        for post in hot_posts:
            message = await ctx.send(post.title)

def setup(bot:commands.Bot):
    bot.add_cog(WikiLeaks(bot))