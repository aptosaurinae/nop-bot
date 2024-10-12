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
parser.add_argument("help_file", type=str, help="Help descriptions")
parser.add_argument("ilvls_file", type=str, help="Itemlevels file for current season")
args = vars(parser.parse_args())
with open(args["token_file"], "rb") as token_file:
    token_data = tomllib.load(token_file)
with open(args["channels_file"], "rb") as channels_file:
    channel_links = tomllib.load(channels_file)
with open(args["help_file"], "rb") as help_file:
    help_data = tomllib.load(help_file)
with open(args["ilvls_file"], "rb") as ilvls_file:
    ilvls_data = tomllib.load(ilvls_file)

TOKEN = token_data["discord"]["token"]
CHANNELS_GENERAL = channel_links["general"]
CHANNELS_RULES = channel_links["rules"]
CHANNELS_BOT = channel_links["bot"]
CHANNELS_RAID = channel_links["raids"]
CHANNELS_DUNGEONS = channel_links["dungeons"]
HELP_STRINGS = help_data["help"]
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
    "nop-bot",
]

COOLDOWN_RATE = 1
COOLDOWN_PER = 60
COOLDOWN_PER_MEME = 300

bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=None
)

@bot.check
def check_commands(ctx: commands.Context):
    return ctx.channel.name in CHANNEL_WHITELIST

# --- Help

@bot.command()
# @commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def help(ctx: commands.Context):
    response = [HELP_STRINGS["prefix"]]
    # if len(ctx.args) == 0:
    #     response.append(HELP_STRINGS["short"])
    # else:
    #     for item in ctx.args:
    #         if item in HELP_STRINGS:
    #             response.append(HELP_STRINGS[item])
    response.append(HELP_STRINGS["short"])
    response.append(HELP_STRINGS["suffix"])
    response = "\n".join(response)
    await ctx.send(response)

@bot.command()
# @commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def helpall(ctx: commands.Context):
    response = [HELP_STRINGS["prefix"], HELP_STRINGS["general"], HELP_STRINGS["dungeons"], HELP_STRINGS["raids"], HELP_STRINGS["suffix"]]
    response = "\n".join(response)
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(response)
    await ctx.send(f"{ctx.author.display_name} please check your DMs for a full help list")

# --- General

@bot.command(help='Where to find role self-assignment')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def roles(ctx: commands.Context):
    response = f"""You can self-assign roles in {CHANNELS_GENERAL["server_guide"]} / {CHANNELS_GENERAL["pick_your_role"]}. Make sure you have emote visibility turned on in the Discord settings."""
    await ctx.send(response)

@bot.command(help='Where rules can be found')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def rules(ctx: commands.Context):
    response = f"""Community wide rules are in {CHANNELS_RULES["server_rules"]} while m+ specific additions are in {CHANNELS_RULES["mplus_rules"]} (see {CHANNELS_RULES["boiler_info"]} for high key specific exclusions to these)."""
    await ctx.send(response)

@bot.command(help='Mod related help')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def mods(ctx: commands.Context):
    response = f"""Please use {CHANNELS_GENERAL["contact_mods"]} for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""
    await ctx.send(response)

@bot.command(help='Information about the guild')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def guild(ctx: commands.Context):
    response = f"""The NoP guild information can be found in the {CHANNELS_GENERAL["guild"]} channel. If you have been declined please make sure you don't already have a character in the guild, and that you've been a NoP member for a month."""
    await ctx.send(response)

@bot.command(help='Recommended addons')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def addons(ctx: commands.Context):
    response = """The recommended addons for use in NoP are:
- `Have We Met?` which will track party members for you
- `LoggerHead` which allows combat and chat logging automatically on entering specific instances
- `Warpdeplete` (or similar) to keep track of Mythic Plus dungeon timers and percentages
- `Mythic Dungeon Tools` to plan out routes through dungeons
- `BigWigs` & `LittleWigs` or `Deadly Boss Mods` for raid and dungeon timers
- `AlterEgo` for tracking m+ and raid progress, and vault completion activities across all your characters
- `WeeklyKnowledge` for tracking profession knowledge across all your characters
"""
    await ctx.send(response)

@bot.command(help='Website information')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def website(ctx: commands.Context):
    response = """The NoP website can be found at [www.no-pressure.eu](https://www.no-pressure.eu)"""
    await ctx.send(response)

@bot.command(help='Recruitment discord link')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def recruitmentdiscord(ctx: commands.Context):
    response = """The recruitment discord can be found [here](https://discord.gg/jx8CXHP)

-# Your experience on linked Discords is not managed by <No Pressure - EU>. <No Pressure - EU> will not be held liable for any interactions, positive or negative, you have on other Discord Servers. Linking to an external Discord Server does not consitute an endorsement by the <No Pressure - EU> Moderation Team for any conduct on such server. Browse at your own risk."""
    await ctx.send(response)

# --- Dungeons

@bot.command(help='Expected minimum ilvls for the current season')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
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
        response = f"""The ilevel minimums this season are:
```- m0:   {MPLUS_ILVLS["m0"]}     - m6:   {MPLUS_ILVLS["m6"]}
- m2:   {MPLUS_ILVLS["m2"]}     - m7:   {MPLUS_ILVLS["m7"]}
- m3:   {MPLUS_ILVLS["m3"]}     - m8:   {MPLUS_ILVLS["m8"]}
- m4:   {MPLUS_ILVLS["m4"]}     - m9:   {MPLUS_ILVLS["m9"]}
- m5:   {MPLUS_ILVLS["m5"]}     - m10:  {MPLUS_ILVLS["m10"]}```
    """
    await ctx.send(response)

@bot.command(help='Experience requirements for mythic plus dungeons')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def mxp(ctx: commands.Context):
    response = """Applications to keys where your experience in that dungeon is 2 or greater below the current key level is a perfectly valid reason for a decline and we recommend you work your way up incrementally 1 level at a time. Using dungeon score (a.k.a. raider.io / RIO score) is not a valid reason to decline an applicant, however experience in that specific dungeon is."""
    await ctx.send(response)

@bot.command(help='Party composition rules')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def mparty(ctx: commands.Context):
    response = """This is a learning community first and foremost, not a pushing community. Declining for party composition reasons is only valid if you want the final player to bring bloodlust (and please decline people kindly if this is the case in line with server rule #1)."""
    await ctx.send(response)

@bot.command(aliases=["db", "buddy"], help='Dungeon Buddy instructions')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def lfg(ctx: commands.Context):
    response = f"""We recommend you review the {CHANNELS_DUNGEONS["get_started"]} before finding groups in NoP. Dungeon Buddy instructions can be found in {CHANNELS_DUNGEONS["db"]}."""
    await ctx.send(response)

# --- Raids

@bot.command(help='How to join raids')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def raidjoin(ctx: commands.Context):
    response = f"""You can find instructions on how to get started with raids in {CHANNELS_RAID["get_started"]}, and sign up to raids in {CHANNELS_RAID["norm_hero"]}. Mythic raids can be found in {CHANNELS_RAID["mythic"]}"""
    await ctx.send(response)

@bot.command(help='How to set up raids')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER, type=commands.BucketType.channel)
async def raidsetup(ctx: commands.Context):
    response = f"""We are always looking for more raid organisers! You can find instructions on how to set up raids in {CHANNELS_RAID["get_started"]}, or if you need more help with setting up a raid helper post then you can use {CHANNELS_RAID["organisation"]} for discussion"""
    await ctx.send(response)

# --- Memes

@bot.command(help='Gold!')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER_MEME, type=commands.BucketType.guild)
async def gold(ctx: commands.Context):
    response = """Maybe <@116233340977152004> can lend you some"""
    await ctx.send(response)

@bot.command(help='Get me a cuppa')
@commands.cooldown(rate=COOLDOWN_RATE, per=COOLDOWN_PER_MEME, type=commands.BucketType.guild)
async def tea(ctx: commands.Context):
    response = f"""*pours {ctx.author.display_name} a cup of tea*"""
    await ctx.send(response)

@bot.command(help='Bans someone?')
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