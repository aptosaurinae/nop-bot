# bot.py
import argparse
import tomllib
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
CHANNELS_GUILD = channel_links["guild"]
MPLUS_ILVLS = ilvls_data["mplus"]
RAID_ILVLS = ilvls_data["raid"]

CHANNEL_WHITELIST = [
    "general-chat",
    "wow-help",
    "sc-social-club",
    "tank",
    "healer",
    "dps",
    "profession-goldmaking",
    "crafting-orders",
    "dungeons-chat",
    "lfg-nm-hc-tw",
    "lfg-m0",
    "lfg-m2-m3",
    "lfg-m4-m6",
    "lfg-m7-m9",
    "lfg-m10",
    "raid-chat",
    "raid-organisation-help",
    "boiler-mplus-chat",
    "lfg-m11-m14",
    "lfg-m15-and-up",
    "boiler-raid-chat",
]

COOLDOWN_RATE = 1
COOLDOWN_PER = 60

bot = commands.Bot(
    command_prefix='!',
    intents=intents
)

@bot.check
def check_commands(ctx: commands.Context):
    return ctx.channel.name in CHANNEL_WHITELIST

cooldown = commands.cooldown(COOLDOWN_RATE, COOLDOWN_PER)

last_messages = {}

@bot.command(help='Expected minimum ilvls for the current season', cooldown=cooldown)
async def ilvl(ctx: commands.Context):
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

@bot.command(help='Where to find role self-assignment', cooldown=cooldown)
async def roles(ctx: commands.Context):
    response = f"""You can self-assign roles in {CHANNELS_ROLES["server_guide"]} / {CHANNELS_ROLES["pick_your_role"]}. Make sure you have emote visibility turned on in the Discord settings."""
    await ctx.send(response)

@bot.command(help='Where rules can be found', cooldown=cooldown)
async def rules(ctx: commands.Context):
    response = f"""Community wide rules are in {CHANNELS_RULES["server_rules"]} while m+ specific additions are in {CHANNELS_RULES["mplus_rules"]} (see {CHANNELS_RULES["boiler_info"]} for high key specific exclusions to these)."""
    await ctx.send(response)

@bot.command(help='Experience requirements for mythic plus dungeons', cooldown=cooldown)
async def mxp(ctx: commands.Context):
    response = """Applications to keys where your experience in that dungeon is 2 or greater below the current key level is a perfectly valid reason for a decline and we recommend you work your way up incrementally 1 level at a time. Using dungeon score (a.k.a. raider.io / RIO score) is not a valid reason to decline an applicant, however experience in that specific dungeon is."""
    await ctx.send(response)

@bot.command(help='Party composition rules', cooldown=cooldown)
async def mparty(ctx: commands.Context):
    response = """This is a learning community first and foremost, not a pushing community. Declining for party composition reasons is only valid if you want the final player to bring bloodlust (and please decline people kindly if this is the case in line with server rule #1)."""
    await ctx.send(response)

@bot.command(help='Mod related help', cooldown=cooldown)
async def mods(ctx: commands.Context):
    response = f"""Please use {CHANNELS_MODS["contact_mods"]} for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""
    await ctx.send(response)

@bot.command(help='Information about the guild', cooldown=cooldown)
async def guild(ctx: commands.Context):
    response = f"""The NoP guild information can be found in the {CHANNELS_GUILD["guild"]} channel. If you have been declined please make sure you don't already have a character in the guild, and that you've been a NoP member for a month."""
    await ctx.send(response)

@bot.command(help='Recommended addons', cooldown=cooldown)
async def addons(ctx: commands.Context):
    response = """The recommended addons for use in NoP are:
- `Have We Met?` which will track party members for you
- `LoggerHead` which allows combat and chat logging automatically on entering specific instances
- `Warpdeplete` (or similar) to keep track of Mythic Plus dungeon timers and percentages
- `Mythic Dungeon Tools` to plan out routes through dungeons
"""
    await ctx.send(response)

bot.run(TOKEN)