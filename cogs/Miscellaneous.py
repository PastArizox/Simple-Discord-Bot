import discord
from discord.colour import Colour
from discord.ext import commands
import random
import json

# Get configuration.json
with open("config.json", "r") as config:
    data = json.load(config)
    PREFIX = data["prefix"]

# Misc class
class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ping command
    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send(f"Pong! `{round(self.client.latency*1000)}ms`")

    # help command
    @commands.command()
    @commands.guild_only()
    async def help(self, ctx, category: str = None):
            embed_help = discord.Embed(
                title = "List of commands",
                description = f"""
                **# Miscellaneous**
                `{PREFIX}help`-Shows a commands list
                `{PREFIX}ping`-Shows ping latency of the bot

                **# Moderation**
                `{PREFIX}kick @user [reason]`-Kick a user
                `{PREFIX}ban @user [reason]`-Ban a user
                `{PREFIX}unban @user.id [reason]`-Unban a user  
                """,
                colour = discord.Colour.green()
            )
            await ctx.send(embed = embed_help)


# Add the class to the cogs
def setup(client):
    client.add_cog(Misc(client))