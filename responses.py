# response strings for the bot
import tomllib

ilvls_file = "ilvls_tww_s1.toml"
with open(ilvls_file, "rb") as ilvls_file:
    ilvls_data = tomllib.load(ilvls_file)

MPLUS_ILVLS = ilvls_data["mplus"]
RAID_ILVLS = ilvls_data["raid"]

channel_server_guide = "<id:guide>"
channel_pick_your_role = "https://discord.com/channels/1055487463734386739/1063229478756696164"
channel_contact_mods = "https://discord.com/channels/1055487463734386739/1063237446042648618"
channel_guild = "https://discord.com/channels/1055487463734386739/1267182548702990377"

channel_rules_server = "https://discord.com/channels/1055487463734386739/1180130833487626300"
channel_rules_mplus = "https://discord.com/channels/1055487463734386739/1290734945156857938"
channel_rules_boiler = "https://discord.com/channels/1055487463734386739/1224353705042907187"

channel_bot_feedback = "https://discord.com/channels/1055487463734386739/1293932439382655098"

channel_dungeon_get_started = "https://discord.com/channels/1055487463734386739/1225062828470173706"
channel_dungeon_buddy = "https://discord.com/channels/1055487463734386739/1225066342106005514"

channel_raid_get_started = "https://discord.com/channels/1055487463734386739/1225062863073312849"
channel_raid_organisation = "https://discord.com/channels/1055487463734386739/1065196123108679700"
channel_raid_norm_hero = "https://discord.com/channels/1055487463734386739/1065699417342099486"
channel_raid_mythic = "https://discord.com/channels/1055487463734386739/1224353658926272522"

# ---
help = {}

help["prefix"] = "The following commands are available (prefixed by `!`):"

help["suffix"] = "-# For more information on individual commands use `helpall` for a full list in a DM"

help["general"] = f"""general:
- `rules` - a refresher on where you can find various rules
- `roles` - pointers to where roles can be self-assigned
- `guild` - a link to the {channel_guild} channel and some reminders of requirements to join the guild
- `mods` - reminders on how you can contact us
- `addons` - recommended addons for WoW
- `website` - a link to the No Pressure website
- `recruitmentdiscord` - a link to the WoW recruitment EU discord
- `newuser` - provides the `rules`, `roles`, `lfg`, and `raidjoin` commands in one
- `newshort` - provides the `lfg`, and `raidjoin` commands in one"""

help["dungeons"] = """dungeons:
- `ilvl` - the minimum ilvls allowed for each m+ difficulty (this adapts depending on which channel it's called in)
- `mxp` - a reminder of the rule about what experience is expected for keys
- `mparty` - a reminder of the rule about who you can decline from keys
- `lfg` - where you can find instructions on how to join dungeons and use the dungeon buddy"""

help["raids"] = """raids:
- `raidjoin` - where to find information about joining raids
- `raidsetup` - where to find information about setting up raids"""

help["short"] = """general: `rules`, `roles`, `guild`, `mods`, `addons`, `website`, `recruitmentdiscord`, `newuser`, `newshort`
dungeons: `ilvl`, `mxp`, `mparty`, `lfg`
raids: `raidjoin`, `raidsetup`"""

# ---
general = {}

general["roles"] = f"""You can self-assign roles in {channel_server_guide} / {channel_pick_your_role}. Make sure you have emote visibility turned on in the Discord settings."""

general["rules"] = f"""Community wide rules are in {channel_rules_server} while m+ specific additions are in {channel_rules_mplus} (see {channel_rules_boiler} for high key specific exclusions to these)."""

general["mods"] = f"""Please use {channel_contact_mods} for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""

general["guild"] = f"""The NoP guild information can be found in the {channel_guild} channel. If you have been declined please make sure you don't already have a character in the guild, and that you've been a NoP member for a month."""

general["addons"] = """The recommended addons for use in NoP are:
- `Have We Met?` which will track party members for you
- `LoggerHead` which allows combat and chat logging automatically on entering specific instances
- `Warpdeplete` (or similar) to keep track of Mythic Plus dungeon timers and percentages
- `Mythic Dungeon Tools` to plan out routes through dungeons
- `BigWigs` & `LittleWigs` or `Deadly Boss Mods` for raid and dungeon timers
- `AlterEgo` for tracking m+ and raid progress, and vault completion activities across all your characters
- `WeeklyKnowledge` for tracking profession knowledge across all your characters
"""

general["website"] = """The NoP website can be found at [www.no-pressure.eu](https://www.no-pressure.eu)"""

general["recruitmentdiscord"] = """The recruitment discord can be found [here](https://discord.gg/jx8CXHP)

-# Your experience on linked Discords is not managed by <No Pressure - EU>. <No Pressure - EU> will not be held liable for any interactions, positive or negative, you have on other Discord Servers. Linking to an external Discord Server does not consitute an endorsement by the <No Pressure - EU> Moderation Team for any conduct on such server. Browse at your own risk."""

# ---
dungeons = {}

dungeons["ilvl_general"] = f"""The ilevel minimums this season are:
```- m0:   {MPLUS_ILVLS["m0"]}     - m6:   {MPLUS_ILVLS["m6"]}
- m2:   {MPLUS_ILVLS["m2"]}     - m7:   {MPLUS_ILVLS["m7"]}
- m3:   {MPLUS_ILVLS["m3"]}     - m8:   {MPLUS_ILVLS["m8"]}
- m4:   {MPLUS_ILVLS["m4"]}     - m9:   {MPLUS_ILVLS["m9"]}
- m5:   {MPLUS_ILVLS["m5"]}     - m10:  {MPLUS_ILVLS["m10"]}```
    """
dungeons["ilvl_m0"] = f"""The expected ilevel minimum for m0 is {MPLUS_ILVLS["m0"]}"""
dungeons["ilvl_m2-m3"] = f"""The expected ilevel minimum for m2 is {MPLUS_ILVLS["m2"]}, and m3 is {MPLUS_ILVLS["m3"]}"""
dungeons["ilvl_m4-m6"] = f"""The expected ilevel minimum for m4 is {MPLUS_ILVLS["m4"]}, m5 is {MPLUS_ILVLS["m5"]}, and m6 is {MPLUS_ILVLS["m6"]}"""
dungeons["ilvl_m7-m9"] = f"""The expected ilevel minimum for m7 is {MPLUS_ILVLS["m7"]}, m8 is {MPLUS_ILVLS["m8"]} and m9 is {MPLUS_ILVLS["m9"]}"""
dungeons["ilvl_m10"] = f"""The expected ilevel minimum for m10 is {MPLUS_ILVLS["m10"]}"""

dungeons["xp"] = """Applications to keys where your experience in that dungeon is 2 or greater below the current key level is a perfectly valid reason for a decline and we recommend you work your way up incrementally 1 level at a time. Using dungeon score (a.k.a. raider.io / RIO score) is not a valid reason to decline an applicant, however experience in that specific dungeon is."""

dungeons["party"] = """This is a learning community first and foremost, not a pushing community. Declining for party composition reasons is only valid if you want the final player to bring bloodlust (and please decline people kindly if this is the case in line with server rule #1)."""

dungeons["lfg"] = f"""We recommend you review the {channel_dungeon_get_started} before finding dungeon groups in NoP. Dungeon Buddy instructions can be found in {channel_dungeon_buddy}."""

# ---
raids = {}

raids["join"] = f"""You can find instructions on how to get started with raids in {channel_raid_get_started}, and sign up to raids in {channel_raid_norm_hero}. Mythic raids can be found in {channel_raid_mythic}"""

raids["setup"] = f"""We are always looking for more raid organisers! You can find instructions on how to set up raids in {channel_raid_get_started}, or if you need more help with setting up a raid helper post then you can use {channel_raid_organisation} for discussion"""

# ---

general["newuser"] = f"""Welcome to No Pressure!
- {general["rules"]}
- {general["roles"]}
- {dungeons["lfg"]}
- {raids["join"]}
-# {general["mods"]}"""

general["newuser_short"] = f"""- {dungeons["lfg"]}
- {raids["join"]}
-# {general["mods"]}"""
