import json
import discord.utils
from keys import discord_role_crew, discord_role_astronaut

LEVEL_UP = [100, 250, 500, 1000, 2500, 5000, 10000]


async def handle_exp(message):

    with open("levels/level.json", "r") as f:

        level_data = json.load(f)
        temp = level_data

    author = str(message.author)

    # Check if user already exists
    if author in level_data:

        exp = level_data[author]["exp"]
        lvl = level_data[author]["lvl"]
        exp += 10

        if exp in LEVEL_UP:
            lvl += 1
            if lvl == 2:
                member = message.author
                role = discord.utils.get(member.guild.roles, id=discord_role_crew)
                await member.add_roles(role)
                await message.channel.send(f"{message.author.mention} You leveled up! You are now lvl {lvl} 🥳 \nNew Rank: Crew Member 🚀")
                print(f">> {author} leveled up to {lvl}")
            elif lvl == 4:
                member = message.author
                role = discord.utils.get(member.guild.roles, id=discord_role_astronaut)
                await member.add_roles(role)
                await message.channel.send(f"{message.author.mention} You leveled up! You are now lvl {lvl} 🥳 \nNew Rank: Astronaut 🚀")
                print(f">> {author} leveled up to {lvl}")
            else:
                await message.channel.send(f"{message.author.mention} You leveled up! You are now lvl {lvl} 🥳 ")
                print(f">> {author} leveled up to {lvl}")

        temp[author] = {}
        temp[author]["exp"] = exp
        temp[author]["lvl"] = lvl

    else:
        temp[author] = {}
        temp[author]["exp"] = 10
        temp[author]["lvl"] = 1

    with open("levels/level.json", "w") as f:
        json.dump(temp, f, indent=4)


async def get_lvl(ctx):
    with open("levels/level.json", "r") as f:
        level_data = json.load(f)
        author = str(ctx.message.author)
        name = author.split("#")[0]

        lvl = level_data[author]["lvl"]
        exp = level_data[author]["exp"]

        em = discord.Embed(color=0xFFD54F)
        em.add_field(name=f"{name} - Level {lvl} ✨", value=f"Exp: {exp}xp")
        await ctx.channel.send(embed=em)

        print(f">> lvl: {lvl}, exp: {exp}")
