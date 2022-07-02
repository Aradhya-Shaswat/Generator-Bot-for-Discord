import discord
from discord.ext import commands
from pretty_help import PrettyHelp, DefaultMenu
import random
import time

bot = commands.Bot(command_prefix='.', case_insensitive=True)

nav = DefaultMenu("◀️", "▶️", "❌")
bot.help_command = PrettyHelp(navigation=nav, color=discord.Colour.green(), no_category="Commands", sort_commands=True, query="Find Help Here.")

@bot.event
async def on_ready():
  print("Bot Ready")

@bot.group(invoke_without_command=True, brief="Gen Command, Can Be Used For mc, netflix & vpn")
async def gen(ctx):
  await ctx.send("``Proper Usage = '.gen mc, netflix, vpn'``")

@gen.command()
async def  mc(ctx, user:discord.Member, *, message=None):
  await ctx.send("Sent Email and Password in DMs !")
  time.sleep(4)
  await user.send("Email: ``null``\nPassword: ``null``")

bot.run(token)
