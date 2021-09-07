# This base has been made by Razmo
# github link : https://github.com/TheRealRazmo

from discord.ext.commands import context
from discord.ext.commands import Context
from discord.ext.commands.core import command
import discord
from discord.ext import commands
import random
import json
import os

# From version 1.5
intents = discord.Intents.default()
intents.presences = True
intents.members = True

# Get config.json
with open("config.json", "r") as config:
    data = json.load(config)
    TOKEN = data["token"]
    PREFIX = data["prefix"]

# Set the client (the bot)
client = commands.Bot(command_prefix=PREFIX, intents=intents)
client.remove_command("help")

# Load the cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Create the on_ready event
@client.event
async def on_ready():
    print("-----------------")
    print("The bot is ready.")
    print("Base made by Razmo")

# Create the on_member join event
@client.event
async def on_member_join(member):
    pass
    # print(f'{member} has joined {member.guild.name}.')

# Create the on_member_remove event
@client.event
async def on_member_remove(member):
    pass
    # print(f'{member} has left {member.guild.name}.')

# Create the on_message event
@client.event
async def on_message(message):
    if message.guild:
        c = message.content # Create a variable to store the content of the message
        c = str(c.lower())
        if message.author != client.user:
            if c == "hello" or c == "hi":
                await message.add_reaction("👋")
                await message.channel.send(f"Hello {message.author.mention}, Im {client.user.name}")
    await client.process_commands(message)

# Handle errors with on_command_error event
@client.event
async def on_command_error(ctx, error):
    try:
        await ctx.message.delete()
    except:
        pass
    if isinstance(error, commands.MissingPermissions):
        embed_error = discord.Embed(
            description = "You are missing permission(s) to run this command."
        )
        await ctx.send(embed = embed_error)
    elif isinstance(error, commands.MemberNotFound):
        embed_error = discord.Embed(
            description = "Member not found."
        )
        await ctx.send(embed = embed_error)
    elif isinstance(error, commands.CommandNotFound):
        embed_error = discord.Embed(
            description = f"Command not found."
        )
        await ctx.send(embed = embed_error)
    elif isinstance(error, commands.CommandOnCooldown):
        embed_error = discord.Embed(
            description = f"{error}"
        )
        await ctx.send(embed = embed_error)
    elif isinstance(error, commands.errors.BadArgument):
        embed_error = discord.Embed(
            description = f"Error found: Bad Argument."
        )
        await ctx.send(embed = embed_error)
    else:
        raise error

# Run the client (the bot)
client.run(TOKEN)