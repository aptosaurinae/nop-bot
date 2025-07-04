# bot.py
try:
    import tomllib
except ModuleNotFoundError:
    import pip._vendor.tomli as tomllib
import argparse
from datetime import timedelta
import discord
from discord.ext import commands
from responses import (
    help as HELP,
    general as GENERAL,
    dungeons as DUNGEONS,
    raids as RAIDS
)

intents = discord.Intents.default()
intents.message_content = True

parser = argparse.ArgumentParser(description="Configuration for discord bot")
parser.add_argument("token_file", type=str, help="Discord Token")

args = vars(parser.parse_args())
with open(args["token_file"], "rb") as token_file:
    token_data = tomllib.load(token_file)

TOKEN = token_data["discord"]["token"]

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
    "lfg-m10-m11",
    "raid-chat",
    "raid-organisation-help",
    "boiler-mplus-chat",
    "boiler-raid-chat",
    "nop-bot",
]

COOLDOWN_RATE = 1
COOLDOWN_HELP = 5
COOLDOWN_PER = 120
COOLDOWN_ILVL = 300
COOLDOWN_PER_MEME = 300

bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=None
)

@bot.check
def check_commands(ctx: commands.Context):
    return type(ctx.channel) is discord.channel.DMChannel or (type(ctx.channel) is discord.channel.TextChannel and ctx.channel.name in CHANNEL_WHITELIST)

def not_dm():
    def predicate(ctx):
        return type(ctx.channel) is not discord.channel.DMChannel
    return commands.check(predicate)

# --- Help

@bot.command()
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_HELP, type=commands.BucketType.channel)
async def help(ctx: commands.Context):
    response = [HELP["prefix"]]
    response.append(HELP["short"])
    response.append(HELP["suffix"])
    response = "\n".join(response)
    await ctx.send(response)

@bot.command()
async def helpall(ctx: commands.Context):
    response = [HELP["prefix"], HELP["general"], HELP["dungeons"], HELP["raids"]]
    response = "\n".join(response)
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(response)
    await ctx.send(f"{ctx.author.display_name} please check your DMs for a full help list")

# --- General

@bot.command(help='Where to find role self-assignment')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def roles(ctx: commands.Context):
    await ctx.send(GENERAL["roles"])

@bot.command(help='Where rules can be found')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def rules(ctx: commands.Context):
    await ctx.send(GENERAL["rules"])

@bot.command(aliases=["report"], help='Mod related help')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def mods(ctx: commands.Context):
    await ctx.send(GENERAL["mods"])

@bot.command(help='Information about the guild')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def guild(ctx: commands.Context):
    await ctx.send(GENERAL["guild"])

@bot.command(help='Recommended addons')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def addons(ctx: commands.Context):
    await ctx.send(GENERAL["addons"], suppress_embeds=True)

@bot.command(help='Website information')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def website(ctx: commands.Context):
    await ctx.send(GENERAL["website"])

@bot.command(aliases=['recruitment','recruitmentdiscord'],help='Links to recruitment areas')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def lfteam(ctx: commands.Context):
    await ctx.send(GENERAL["lfteam"])

@bot.command(help='Provides the `rules`, `roles`, `lfg` and `raidjoin` commands in one response')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def newuser(ctx: commands.Context):
    await ctx.send(GENERAL["newuser"])

@bot.command(aliases=["new"], help='Provides the `lfg` and `raidjoin` commands in one response')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def newshort(ctx: commands.Context):
    await ctx.send(GENERAL["newuser_short"])

@bot.command(aliases=["craftingorders", "craftingorder", "craftserver", "craftorder", "craftorders"], help='Information on placing crafting orders in NoP')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def craft(ctx: commands.Context):
    await ctx.send(GENERAL["craft"])

@bot.command(aliases=["wayfarersrefuge", "nadiscord", "wayfarers"], help='Link to The Wayfarers Refuge North America discord')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def twr(ctx: commands.Context):
    await ctx.send(GENERAL["wayfarers"])

@bot.command(aliases=["todayinwow"], help='Link to the WoWhead Today in WoW page')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def today(ctx: commands.Context):
    await ctx.send(GENERAL["today"])

@bot.command(aliases=["classicmop", "mop"], help='Link to the "Not our Patch" discord')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def classic(ctx: commands.Context):
    await ctx.send(GENERAL["classic"])

# --- Dungeons

@bot.command(aliases=["ilevel", "itemlevel"], help='Guideline ilvls for the current season')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_ILVL, type=commands.BucketType.channel)
async def ilvl(ctx: commands.Context):
    addendum = True
    if type(ctx.channel) is discord.channel.TextChannel:
        if ctx.channel.name == "lfg-m0":
            response = DUNGEONS["ilvl_m0"]
        elif ctx.channel.name == "lfg-m2-m3":
            response = DUNGEONS["ilvl_m2-m3"]
        elif ctx.channel.name == "lfg-m4-m6":
            response = DUNGEONS["ilvl_m4-m6"]
        elif ctx.channel.name == "lfg-m7-m9":
            response = DUNGEONS["ilvl_m7-m9"]
        elif ctx.channel.name == "lfg-m10-m11":
            response = DUNGEONS["ilvl_m10"]
        elif ctx.channel.name in ["raid-chat", "raid-organisation-help", "boiler-raid-chat"]:
            response = RAIDS["ilvl"]
            addendum = False
        else:
            response = DUNGEONS["ilvl_general"]
    else:
        response = DUNGEONS["ilvl_general"]
    if addendum:
        response = f'{response}\n{DUNGEONS["ilvl_channel_addendum"]}'
    await ctx.send(response)

@bot.command(help='Experience requirements for mythic plus dungeons')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def mxp(ctx: commands.Context):
    await ctx.send(DUNGEONS["xp"])

@bot.command(help='Party composition rules')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def mparty(ctx: commands.Context):
    await ctx.send(DUNGEONS["party"])

@bot.command(aliases=["db", "buddy"], help='Dungeon Buddy instructions')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def lfg(ctx: commands.Context):
    await ctx.send(DUNGEONS["lfg"])

@bot.command(aliases=["completion"], help='Information on whether to pick Time or Completion for key posts')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def time(ctx: commands.Context):
    await ctx.send(DUNGEONS["time"])

@bot.command(aliases=["dungeontemplate"], help='Looking for Group non-dungeon-buddy template')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def lfgtemplate(ctx: commands.Context):
    await ctx.send(DUNGEONS["lfgtemplate"])

@bot.command(aliases=["mythicplus"], help='Link to the mythicpl.us website')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def affix(ctx: commands.Context):
    await ctx.send(DUNGEONS["affix"])

# --- Raids

@bot.command(aliases=["raid"], help='How to join raids')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def raidjoin(ctx: commands.Context):
    await ctx.send(RAIDS["join"])

@bot.command(aliases=["raidlead"], help='How to set up raids')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def raidsetup(ctx: commands.Context):
    await ctx.send(RAIDS["setup"])

# --- Memes

@bot.command(help='Gold!')
@not_dm()
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER_MEME, type=commands.BucketType.guild)
async def gold(ctx: commands.Context):
    response = """Maybe <@116233340977152004> can lend you some"""
    await ctx.send(response)

@bot.command(help='Get me a cuppa')
@not_dm()
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER_MEME, type=commands.BucketType.guild)
async def tea(ctx: commands.Context):
    response = f"""*pours {ctx.author.display_name} a cup of tea*"""
    await ctx.send(response)

@bot.command(help='Bans someone?')
@not_dm()
@commands.cooldown(rate=COOLDOWN_RATE, per=3600, type=commands.BucketType.guild)
async def ban(ctx: commands.Context):
    response = """Time for a ban!"""
    poll = discord.Poll(
        question=f"How long should we ban {ctx.author.display_name} for?",
        duration=timedelta(hours=1)) # discord polls have to be in whole-number hours
    poll.add_answer(text="1 hour")
    poll.add_answer(text="1 day")
    poll.add_answer(text="Forever")
    await ctx.send(response, poll=poll)

# ---

bot.run(TOKEN)