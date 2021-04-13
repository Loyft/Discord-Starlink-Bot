import time
import discord
from discord.ext import commands, tasks
from reddit_commands import *
from datetime import datetime

TOKEN = discord_bot_token

bot = commands.Bot(command_prefix="_")


@bot.event
async def on_ready():
    guilds = list(bot.guilds)
    print(f"{bot.user} has connected to:\n")
    for n in range(len(guilds)):
        print(" " + guilds[n-1].name)
    top_post_space.start()
    top_post_spacex.start()
    top_post_nasa.start()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the Stars ✨"))


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
    name = h_post.title
    url = h_post.url
    em = discord.Embed(title=name, description=url, color=0x4964d0)
    em.set_image(url=url)
    await ctx.send(embed=em)


@bot.command(name="help", help="Shows Starlink Bot info")
async def commands(ctx):
    current_time = str(datetime.now()).split(".")[0]
    print(f"[{current_time}] {ctx.guild}: {ctx.author} = {ctx.message.content}")
    desc_text = "**prefix: _**\n\n_commands: Shows commands for Starlink Bot\n_inv:  Shows invite link for Starlink Bot"
    em = discord.Embed(description=desc_text, color=0x4964d0)
    em.set_author(name="Commands")
    em.set_footer(text="Starlink Bot made with ♥️ by Loyft#6709")
    await ctx.send(embed=em)


# Get Space subreddit top post past 8 hours
@tasks.loop(hours=8)
async def top_post_space():
    time.sleep(1800)
    space_top = get_top("space", "day")
    if space_top:
        space_name = space_top.title
        space_url = space_top.url
        space_em = discord.Embed(title=space_name, description=space_url, color=0x4964d0)
        space_em.set_image(url=space_url)
        space_channel = bot.get_channel(831215986782371880)
        await space_channel.send(embed=space_em)


# Get SpaceX subreddit top post past 8 hours
@tasks.loop(hours=36)
async def top_post_spacex():
    time.sleep(1800)
    spacex_top = get_top("spacex", "week")
    if spacex_top:
        spacex_name = spacex_top.title
        spacex_url = spacex_top.url
        spacex_em = discord.Embed(title=spacex_name, description=spacex_url, color=0x4964d0)
        spacex_em.set_image(url=spacex_url)
        spacex_channel = bot.get_channel(831216182941057145)
        await spacex_channel.send(embed=spacex_em)


# Get SpaceX subreddit top post past 8 hours
@tasks.loop(hours=12)
async def top_post_nasa():
    time.sleep(1800)
    nasa_top = get_top("nasa", "week")
    if nasa_top:
        nasa_name = nasa_top.title
        nasa_url = nasa_top.url
        nasa_em = discord.Embed(title=nasa_name, description=nasa_url, color=0x4964d0)
        nasa_em.set_image(url=nasa_url)
        nasa_channel = bot.get_channel(831216264105295912)
        await nasa_channel.send(embed=nasa_em)

bot.run(TOKEN)
