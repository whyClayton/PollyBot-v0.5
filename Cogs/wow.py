import discord
from discord.ext import commands
import time
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='PollyBot')
hot_posts = reddit.subreddit('wow').hot(limit=10)

class wownews(commands.Cog, name="reddit wow news"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "wownews",
                    usage="",
                    description = "Shows the top ten posts on /r/wow")
    #Function that will post the top 10 posts from /r/energy
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def energynews(self, ctx):
        for post in hot_posts:
            message = await ctx.send(post.title)
            await message.edit(content=f" • " + post.title)
            print("worked.")

def setup(bot:commands.Bot):
    bot.add_cog(wownews(bot))