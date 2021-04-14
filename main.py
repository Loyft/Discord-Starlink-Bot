import time
import discord
from discord.ext import commands, tasks
from pr0_commands import get_pr0_posts
from reddit_commands import *
from datetime import datetime

TOKEN = discord_bot_token
CHAN_SPACE = discord_channel_space_id
CHAN_SPACEX = discord_channel_spacex_id
CHAN_NASA = discord_channel_nasa_id
CHAN_WELT = discord_channel_welt_id

bot = commands.Bot(command_prefix="_")


# On Start up
@bot.event
async def on_ready():
    guilds = list(bot.guilds)
    print(f"{bot.user} has connected to:\n")
    for n in range(len(guilds)):
        print(" " + guilds[n-1].name)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the Stars ✨"))

    # Wait 1min before starting tasks to fetch news
    time.sleep(60)
    top_post_space.start()
    top_post_spacex.start()
    top_post_nasa.start()
    pr0_weltraum.start()


# Commands
@bot.command(name="inv", help="Shows invite link for Starlink Bot")
async def inv(ctx):
    print(f"{ctx.guild}: {ctx.author} = {ctx.message.content}")
    response = "https://discord.com/oauth2/authorize?client_id=830872756198309951&scope=bot"
    await ctx.send(response)
    print(f">> {response}")


@bot.command(name="space", help="Get top post from Space subreddit")
async def space(ctx):
    print(f"{ctx.guild}: {ctx.author} = {ctx.message.content}")
    h_post = get_top("space", "day")
    url = h_post.url
    await ctx.send(url)


@bot.command(name="info", help="Shows Starlink Bot info")
async def commands(ctx):
    current_time = str(datetime.now()).split(".")[0]
    print(f"[{current_time}] {ctx.guild}: {ctx.author} = {ctx.message.content}")
    em = discord.Embed(color=0x4964d0)
    em.add_field(name="Commands", value="_info\n_inv", inline=False)
    em.add_field(name="News", value="gets the newest top posts from r/space, r/spacex and r/nasa", inline=False)
    em.add_field(name="About", value="made with ♥️ by Loyft#6709", inline=False)
    em.set_footer(text="https://github.com/Mizuyi/Discord-Starlink-Bot")
    await ctx.send(embed=em)


# Scheduled events
# Get pr0 weltraum posts every 10 hours
@tasks.loop(hours=10)
async def pr0_weltraum():
    url_list = get_pr0_posts()
    weltraum_channel = bot.get_channel(CHAN_WELT)
    for item in url_list:
        await weltraum_channel.send(item)


# Get Space subreddit top post past 15 hours
@tasks.loop(hours=15)
async def top_post_space():
    space_top = get_top("space", "day")
    if space_top:
        space_url = space_top.url
        space_channel = bot.get_channel(CHAN_SPACE)
        await space_channel.send(space_url)


# Get SpaceX subreddit top post past 35 hours
@tasks.loop(hours=35)
async def top_post_spacex():
    spacex_top = get_top("spacex", "week")
    if spacex_top:
        spacex_url = spacex_top.url
        spacex_channel = bot.get_channel(CHAN_SPACEX)
        await spacex_channel.send(embed=spacex_url)


# Get SpaceX subreddit top post past 15 hours
@tasks.loop(hours=15)
async def top_post_nasa():
    nasa_top = get_top("nasa", "week")
    if nasa_top:
        nasa_url = nasa_top.url
        nasa_channel = bot.get_channel(CHAN_NASA)
        await nasa_channel.send(embed=nasa_url)

bot.run(TOKEN)
