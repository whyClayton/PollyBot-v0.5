import discord
from discord.ext import commands
import time
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
hot_posts = reddit.subreddit('nba').hot(limit=10)

class nbanews(commands.Cog, name="reddit nba news"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "nbanews",
                    usage="",
                    description = "Shows the top ten posts on /r/nba")
    #Function that will post the top 10 posts from /r/energy
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def energynews(self, ctx):
        for post in hot_posts:
            message = await ctx.send(post.title)
            await message.edit(content=f" • " + post.title)
            print("worked.")



def setup(bot:commands.Bot):
    bot.add_cog(nbanews(bot))