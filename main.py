import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import youtube_dl

load_dotenv()

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!")


DISCORD_TOKEN = os.getenv("YOUR TOKEN HERE")


@bot.command(
    help="!setprefix ()your prefix, will set new prefix",
    brief="Wanna set a new prefix?"
)
async def setprefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f"Prefix changed to ``{prefix}``")


@bot.command(
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    brief="Do it I dare u!"
)
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(
    help="Looks like you need some help.",
    brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
    response = ""

    for arg in args:
        response = response + " " + arg

    await ctx.channel.send(response)


@bot.command(help="Prints details of Server", brief="Wanna see the details?")
async def where_am_i(ctx):
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc = ctx.guild.description

    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    members = []
    async for member in ctx.guild.fetch_members(limit=150):
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name, str(member.status),
                                                                       str(member.joined_at)))


@bot.command(help="Info about Mr.Bot", brief="Info about Mr.Bot")
async def tell_me_about_yourself(ctx):
    text = "Hello, My name is Mr.Bot and I am a bot:), type help for more info!"
    await ctx.send(text)


if __name__ == "__main__":
    bot.run(YOUR TOKEN HERE)
