import time
import discord
from discord.ext import commands, tasks
from news.pr0_commands import get_pr0_posts
from news.reddit_commands import *
from news.twitter_commands import get_tweets
from news.insta_commands import get_insta_posts
from levels.level import handle_exp, get_lvl
from commands.iss import get_iss_pos
from datetime import datetime
from reactions import check_for_reaction

TOKEN = discord_bot_token
CHAN_SPACEX = discord_channel_spacex_id
CHAN_WELT = discord_channel_welt_id
CHAN_TWITTER = discord_channel_twitter

bot = commands.Bot(command_prefix="_")


# On Start up
@bot.event
async def on_ready():
    guilds = list(bot.guilds)
    print(f"{bot.user} has connected to:\n")
    for n in range(len(guilds)):
        print("  " + guilds[n-1].name)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the Stars ✨"))

    # Wait 10 seconds before starting tasks to fetch news
    time.sleep(10)
    top_post_spacex.start()
    pr0_weltraum.start()
    get_all_tweets.start()
    get_insta.start()


# On message
@bot.event
async def on_message(message):

    # Check for reaction
    reaction = check_for_reaction(message.content)
    if reaction:
        await message.add_reaction(reaction)
    else:
        pass

    # Handle Exp
    await handle_exp(message)

    await bot.process_commands(message)


# Commands
@bot.command(name="inv", help="Shows invite link for Starlink Bot")
async def inv(ctx):
    print(f"{ctx.guild}: {ctx.author} = {ctx.message.content}")
    response = "https://discord.com/oauth2/authorize?client_id=830872756198309951&scope=bot"
    await ctx.send(response)
    print(f">> {response}")


@bot.command(name="lvl", help="Shows current level")
async def inv(ctx):
    print(f"{ctx.guild}: {ctx.author} = {ctx.message.content}")
    await get_lvl(ctx)


@bot.command(name="poll", help="Creates a poll.")
async def poll(ctx):
    print(f"{ctx.guild}: {ctx.author} = {ctx.message.content}")
    poll_message_separate = ctx.message.content.split(",")
    poll_question_list = poll_message_separate[0].split(" ")[1:]
    poll_question = ' '.join(poll_question_list)
    poll_answers = poll_message_separate[1:]
    print(poll_question)

    em = discord.Embed(title="🗳", color=0x4964d0)
    em.add_field(name="POLL", value=f"{poll_question}")
    msg = await ctx.channel.send(embed=em)
    for answer in poll_answers:
        react_answer = answer.replace(" ", "")
        await msg.add_reaction(f"{react_answer}")


@bot.command(name="iss")
async def iss(ctx):
    print(f"{ctx.guild}: {ctx.author} = {ctx.message.content}")
    response = get_iss_pos()
    em = discord.Embed(title="🛰 ISS current location 🎯", color=0x4964d0)
    em.add_field(name=f"{response['label']}", value=f"latitude: {response['latitude']}\nlongitude: {response['longitude']}")
    await ctx.send(embed=em)
    print(f">> {response['label']}")


@bot.command(name="info", help="Shows Starlink Bot info")
async def commands(ctx):
    current_time = str(datetime.now()).split(".")[0]
    print(f"[{current_time}] {ctx.guild}: {ctx.author} = {ctx.message.content}")
    em = discord.Embed(color=0x4964d0)
    em.add_field(name="Commands", value="_info\n_iss\n_poll\n_lvl", inline=False)
    em.add_field(name="News", value="gets top space info from various news sources", inline=False)
    em.add_field(name="ISS", value="gets the current ISS location", inline=False)
    em.add_field(name="Poll", value="Creates a poll. (answers must be emotes)\nFormat: '_poll <question>, <answer1>, <answer2>'\nExample: _poll Yes or No?, 👍, 👎", inline=False)
    em.add_field(name="Level", value="Level System: gain experience for activity on the server\nand level up to get exclusive roles.")
    em.add_field(name="About", value="made with ♥️ by Loyft#6709", inline=False)
    em.set_footer(text="https://github.com/Loyft/Discord-Starlink-Bot")
    await ctx.send(embed=em)


# Scheduled events
# Get tweets
@tasks.loop(minutes=15)
async def get_all_tweets():
    tweet_list = get_tweets("elonmusk")
    if tweet_list:
        twitter_channel = bot.get_channel(CHAN_TWITTER)
        for tweet in tweet_list:
            await twitter_channel.send(tweet)
    else:
        pass


# Get pr0 weltraum posts every 5 hours
@tasks.loop(hours=5)
async def pr0_weltraum():
    url_list = get_pr0_posts()
    weltraum_channel = bot.get_channel(CHAN_WELT)
    if url_list:
        for item in url_list:
            await weltraum_channel.send(item)
    else:
        pass


# Get SpaceX subreddit top post past hour
@tasks.loop(hours=1)
async def top_post_spacex():
    spacex_top = get_top("spacex", "week")
    if spacex_top:
        spacex_url = spacex_top.url
        spacex_channel = bot.get_channel(CHAN_SPACEX)
        await spacex_channel.send(spacex_url)
    else:
        pass


# Get lilmayo poasts from insta every 5 hour
@tasks.loop(hours=5)
async def get_insta():
    user = "lilmayo"
    new_posts = get_insta_posts(user)
    if new_posts:
        lilmayo_channel = bot.get_channel(discord_channel_lilmayo)
        for post in new_posts:
            await lilmayo_channel.send(file=discord.File(f"lilmayo/{post}"))
    else:
        pass

bot.run(TOKEN)
