# bot.py
import argparse
import tomllib
from datetime import timedelta
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

parser = argparse.ArgumentParser(description="Configuration for discord bot")
parser.add_argument("token_file", type=str, help="Discord Token")
args = vars(parser.parse_args())
with open(args["token_file"], "rb") as token_file:
    token_data = tomllib.load(token_file)

TOKEN = token_data["discord"]["token"]

bot = commands.Bot(
    command_prefix='!',
    intents=intents
)

last_messages = {}

def throttled(
        ctx: commands.Context,
        msg_type: str,
        throttle_timer = 30
) -> bool:
    """Checks if a previous bot message was sent to the specified channel
    within the global throttle timer

    Args:
        ctx: Context for the message
        throttle_timer: time in seconds to check for the previous message
    """
    global last_messages
    if ctx.channel.name in last_messages:
        if msg_type in last_messages[ctx.channel.name]:
            if (
                    ctx.message.created_at - last_messages[ctx.channel.name][msg_type]
                    <= timedelta(seconds=throttle_timer)):
                return True
    else:
        last_messages[ctx.channel.name] = {}
    last_messages[ctx.channel.name][msg_type] = ctx.message.created_at
    return False

@bot.command(help='Responds with the expected minimum ilvls for the current season')
async def ilvl(ctx: commands.Context):
    if not throttled(ctx, "ilvl"):
        if ctx.channel.name == "lfg-m0":
            response = "The expected ilevel minimum for m0 is 583"
        elif ctx.channel.name == "lfg-m2-m3":
            response = "The expected ilevel minimum for m2/3 is 587"
        elif ctx.channel.name == "lfg-m4-m6":
            response = "The expected ilevel minimum for m4 is 590, m5 is 593, and m6 is 596"
        elif ctx.channel.name == "lfg-m7-m9":
            response = "The expected ilevel minimum for m7/8 is 605, and m9 is 608"
        elif ctx.channel.name == "lfg-m10":
            response = "The expected ilevel minimum for m10 is 608"
        else:
            response = """The expected ilevel minimums this season are:
- m0:   583
- m2/3: 587
- m4:   590
- m5:   593
- m6:   596
- m7/8: 605
- m9+:  608
        """
        await ctx.send(response)

@bot.command(help='Responds with where to find role self-assignment')
async def roles(ctx):
    if not throttled(ctx, "roles"):
        response = """You can self-assign roles in #server-guide / https://discord.com/channels/1292467452688465920/1293172035706556416. Make sure you have emote visibility turned on in the Discord settings."""
        await ctx.send(response)

@bot.command(help='Responds with where rules can be found')
async def rules(ctx):
    if not throttled(ctx, "rules"):
        response = """Community wide rules are in https://discord.com/channels/1292467452688465920/1293173265073705032 while m+ specific additions are in #get-started-dungeons (see #boiler-info for high key specific exclusions to these)."""
        await ctx.send(response)

@bot.command(help='Responds with mod related help')
async def mods(ctx):
    if not throttled(ctx, "mods"):
        response = """Please use #contact-mods for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""
        await ctx.send(response)

bot.run(TOKEN)