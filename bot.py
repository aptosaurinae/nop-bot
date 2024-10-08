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
parser.add_argument("channels_file", type=str, help="Discord Channel Links")
parser.add_argument("ilvls_file", type=str, help="Itemlevels file for current season")
args = vars(parser.parse_args())
with open(args["token_file"], "rb") as token_file:
    token_data = tomllib.load(token_file)
with open(args["channels_file"], "rb") as channels_file:
    channel_links = tomllib.load(channels_file)
with open(args["ilvls_file"], "rb") as ilvls_file:
    ilvls_data = tomllib.load(ilvls_file)

TOKEN = token_data["discord"]["token"]
CHANNELS_ROLES = channel_links["roles"]
CHANNELS_RULES = channel_links["rules"]
CHANNELS_MODS = channel_links["mods"]
MPLUS_ILVLS = ilvls_data["mplus"]
RAID_ILVLS = ilvls_data["raid"]

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
            response = f"""The expected ilevel minimum for m0 is {MPLUS_ILVLS["m0"]}"""
        elif ctx.channel.name == "lfg-m2-m3":
            response = f"""The expected ilevel minimum for m2 is {MPLUS_ILVLS["m2"]}, and m3 is {MPLUS_ILVLS["m3"]}"""
        elif ctx.channel.name == "lfg-m4-m6":
            response = f"""The expected ilevel minimum for m4 is {MPLUS_ILVLS["m4"]}, m5 is {MPLUS_ILVLS["m5"]}, and m6 is {MPLUS_ILVLS["m6"]}"""
        elif ctx.channel.name == "lfg-m7-m9":
            response = f"""The expected ilevel minimum for m7 is {MPLUS_ILVLS["m7"]}, m8 is {MPLUS_ILVLS["m8"]} and m9 is {MPLUS_ILVLS["m9"]}"""
        elif ctx.channel.name == "lfg-m10":
            response = f"""The expected ilevel minimum for m10 is {MPLUS_ILVLS["m10"]}"""
        else:
            response = f"""The expected ilevel minimums this season are:
- m0:   {MPLUS_ILVLS["m0"]}
- m2:   {MPLUS_ILVLS["m2"]}
- m3:   {MPLUS_ILVLS["m3"]}
- m4:   {MPLUS_ILVLS["m4"]}
- m5:   {MPLUS_ILVLS["m5"]}
- m6:   {MPLUS_ILVLS["m6"]}
- m7:   {MPLUS_ILVLS["m7"]}
- m8:   {MPLUS_ILVLS["m8"]}
- m9:   {MPLUS_ILVLS["m9"]}
- m10:  {MPLUS_ILVLS["m10"]}
        """
        await ctx.send(response)

@bot.command(help='Responds with where to find role self-assignment')
async def roles(ctx):
    if not throttled(ctx, "roles"):
        response = f"""You can self-assign roles in {CHANNELS_ROLES["server_guide"]} / {CHANNELS_ROLES["pick_your_role"]}. Make sure you have emote visibility turned on in the Discord settings."""
        await ctx.send(response)

@bot.command(help='Responds with where rules can be found')
async def rules(ctx):
    if not throttled(ctx, "rules"):
        response = f"""Community wide rules are in {CHANNELS_RULES["server_rules"]} while m+ specific additions are in {CHANNELS_RULES["mplus_rules"]} (see {CHANNELS_RULES["boiler_info"]} for high key specific exclusions to these)."""
        await ctx.send(response)

@bot.command(help='Responds with mod related help')
async def mods(ctx):
    if not throttled(ctx, "mods"):
        response = f"""Please use {CHANNELS_MODS["contact_mods"]} for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""
        await ctx.send(response)

bot.run(TOKEN)