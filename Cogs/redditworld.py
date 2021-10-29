import discord
from discord.ext import commands
import time
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
hot_posts = reddit.subreddit('worldnews').hot(limit=10)

class redditworld(commands.Cog, name="reddit politics news"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "redditworld",
                    usage="",
                    description = "Shows the top ten posts on /r/worldnews.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    #Function that will post the top 10 posts from /r/worldnews
    async def redditworld(self, ctx):
        for post in hot_posts:
            message = await ctx.send(post.title)
            await message.edit(content=f" • " + post.title)
            print("worked.")



def setup(bot:commands.Bot):
    bot.add_cog(redditworld(bot))