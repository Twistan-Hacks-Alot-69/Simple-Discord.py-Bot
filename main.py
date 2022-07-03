# This Bot uses command_prefixes!

import discord
from discord.ext import commands
import asyncio
import os


bot = commands.Bot(command_prefix="!") # Feel free to change prefix from "!" to whatever youd like simply just by changing the, !

bot.command 
# bot.command specifys that it is indeed command and that the bot is now looking for a command
async def ping(ctx):
    # ctx is the command_prefix right before in the case ping (So the bot will only look at it if it has the prefix before it)
    await ctx.channel.send("pong")
    # The bot will sennd "pong" back to you in the same channel
    # the middle word is where the bot will be sending "pong" You can change this to "ctx.author.send" to make the bot DM you, "pong"

bot.run("YOUR TOKEN HERE")
# To find your bot token you must create a bot on discord developeer 
# Also for python begginers make sure to use "" between your Token
# This is a VERY basic/simple bot, feel free to add on or modify this bot
