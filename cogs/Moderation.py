import discord
from discord.ext import commands
import random
import json
from discord.ext.commands.core import guild_only

# Get config.json
with open("config.json", "r") as config:
    data = json.load(config)
    TOKEN = data["token"]
    PREFIX = data["prefix"]


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Kick command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member=None, *, reason="Unspecified reason."):
        if user==None:
            embed_error_nouser=discord.Embed(
                description=f"Command usage: {PREFIX}kick @user [reason]"
            )
            await ctx.send(embed=embed_error_nouser)
        elif user==ctx.author:

            embed_error_selfkick=discord.Embed(
                description = "You can't kick yourself."
            )
            await ctx.send(embed=embed_error_selfkick)
        elif user.guild_permissions.kick_members:
            embed_error_perm_user=discord.Embed(
                description="You can't kick this user.",
                colour=0xffffff,
            )
            await ctx.send(embed=embed_error_perm_user)
        else:
            embed_kick=discord.Embed(
                title="Member kicked from the server",
                description=f"{user} has been kicked.",
                colour=discord.Colour.orange()
            )
            await user.kick(reason=reason)
            await ctx.send(embed = embed_kick)

    # Ban command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member=None, *, reason="Unspecified reason."):
        if user==None:
            embed_error_nouser=discord.Embed(
                description=f"Command usage: {PREFIX}ban @user [reason]"
            )
            await ctx.send(embed=embed_error_nouser)
        elif user==ctx.author:

            embed_error_selfban=discord.Embed(
                description = "You can't ban yourself."
            )
            await ctx.send(embed=embed_error_selfban)
        elif user.guild_permissions.ban_members:
            embed_error_perm_user=discord.Embed(
                description="You can't ban this user.",
                colour=0xffffff,
            )
            await ctx.send(embed=embed_error_perm_user)
        else:
            embed_ban=discord.Embed(
                title="Member banned from the server",
                description=f"{user} has been banned.",
                colour=discord.Colour.red()
            )
            await user.ban(reason=reason)
            await ctx.send(embed = embed_ban)

    # Unban command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user=None, *, reason="Unspecified reason."):
        if not user:
            embed_error_nouser = discord.Embed(
                description = f"Command usage: {PREFIX}unban [user.id] [reason]"
            )
            await ctx.send(embed = embed_error_nouser)
        try:
            user = await self.client.fetch_user(int(user))
            await ctx.guild.unban(user, reason = reason)
            embed_unban = discord.Embed(
                title = "Unbanned user",
                description = f"{user} has been unbanned.",
                colour = discord.Colour.green()
            )
            await ctx.send(embed = embed_unban)
        except:
            embed_error_usernotfound = discord.Embed(
                description = f"User not banned."
            )
            await ctx.send(embed = embed_error_usernotfound)

    # Clear command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 15):
        deleted  = await ctx.channel.purge(limit=amount+1)
        msg = await ctx.send("Deleted `{}` message(s)".format(len(deleted)-1))
        await msg.delete(delay=2)


# Add the class to the cogs
def setup(client):
    client.add_cog(Moderation(client))