# response strings for the bot
import tomllib

ilvls_file = "ilvls_tww_s1.toml"
with open(ilvls_file, "rb") as ilvls_file:
    ilvls_data = tomllib.load(ilvls_file)

MPLUS_ILVLS = ilvls_data["mplus"]
RAID_ILVLS = ilvls_data["raid"]

channel_channels_and_roles = "<id:customize>"
channel_pick_your_role = "https://discord.com/channels/1055487463734386739/1063229478756696164"
channel_contact_mods = "https://discord.com/channels/1055487463734386739/1063237446042648618"
channel_guild = "https://discord.com/channels/1055487463734386739/1267182548702990377"
channel_crafting_orders = "https://discord.com/channels/1055487463734386739/1065175223927853107"

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

help["suffix"] = "-# - For more information on individual commands use `helpall` for a full list in a DM"

help["general"] = f"""general:
- `rules` - a refresher on where you can find various rules
- `roles` - pointers to where roles can be self-assigned
- `guild` - a link to the {channel_guild} channel and some reminders of requirements to join the guild
- `mods` - reminders on how you can contact us
- `addons` - recommended addons for WoW
- `website` - a link to the No Pressure website
- `recruitmentdiscord` - a link to the WoW recruitment EU discord
- `newuser` - provides the `rules`, `roles`, `lfg`, and `raidjoin` commands in one
- `newshort` - provides the `lfg`, and `raidjoin` commands in one
- `craft` - provides info on placing crafting orders in NoP"""

help["dungeons"] = """dungeons:
- `ilvl` - the minimum ilvls allowed for each m+ difficulty (this adapts depending on which channel it's called in)
- `mxp` - a reminder of the rule about what experience is expected for keys
- `mparty` - a reminder of the rule about who you can decline from keys
- `lfg` - where you can find instructions on how to join dungeons and use the dungeon buddy"""

help["raids"] = """raids:
- `raidjoin` - where to find information about joining raids
- `raidsetup` - where to find information about setting up raids"""

help["short"] = """- general: `rules`, `roles`, `guild`, `mods`, `addons`, `website`, `recruitmentdiscord`, `newuser`, `newshort`, `craft`
- dungeons: `ilvl`, `mxp`, `mparty`, `lfg`
- raids: `raidjoin`, `raidsetup`"""

# ---
general = {}

general["roles"] = f"""You can customise channels and self-assign roles in {channel_channels_and_roles} / {channel_pick_your_role}. Make sure you have emote visibility turned on in the Discord settings."""

general["rules"] = f"""Community wide rules can be found in {channel_rules_server} while m+ specific additions can be found in {channel_rules_mplus} (see {channel_rules_boiler} for high key specific exclusions to these)."""

general["mods"] = f"""Please use {channel_contact_mods} for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""

general["guild"] = f"""The NoP guild information can be found in the {channel_guild} channel.
You can only have one character in the guild, and you need to have been a NoP discord member for a month for an application to be accepted.

If you have applied and are waiting for an invite, please note that we are volunteer moderators with a few checks to make for every applicant. We will get to your application but it might take a couple of days so please be patient."""

general["addons"] = """The recommended addons for use in NoP are:
- `Have We Met?` which will track party members for you
- `LoggerHead` which allows combat and chat logging automatically on entering specific instances
- `AlterEgo` for tracking m+ and raid progress, and vault completion activities across all your characters
- `WeeklyKnowledge` for tracking profession knowledge across all your characters
- `Warpdeplete` (or similar) to keep track of Mythic Plus dungeon timers and percentages
- `Mythic Dungeon Tools` to plan out routes through dungeons
- `BigWigs` & `LittleWigs` or `Deadly Boss Mods` for raid and dungeon timers
- `Weakauras` is a customisable system for displaying information. You can find setups others have created at [wago.io](https://www.wago.io)"""

general["website"] = """The NoP website can be found at [no-pressure.eu](https://www.no-pressure.eu)"""

general["recruitmentdiscord"] = """The recruitment discord can be found [here](https://discord.gg/jx8CXHP)

-# Your experience on linked Discords is not managed by <No Pressure - EU>. <No Pressure - EU> will not be held liable for any interactions, positive or negative, you have on other Discord Servers. Linking to an external Discord Server does not consitute an endorsement by the <No Pressure - EU> Moderation Team for any conduct on such server. Browse at your own risk."""

general["craft"] = f"""You can find crafting orders in {channel_crafting_orders}. If you are trying to find someone to do a craft for you, **please state your server** as crafts are not region-wide. You can check the pins in the channel for a profession sheet where you might be able to find a crafter for your realm."""

# ---
dungeons = {}

dungeons["ilvl_general"] = f"""The ilevel minimums this season are:
```- m0:   {MPLUS_ILVLS["m0"]}     - m6:   {MPLUS_ILVLS["m6"]}
- m2:   {MPLUS_ILVLS["m2"]}     - m7:   {MPLUS_ILVLS["m7"]}
- m3:   {MPLUS_ILVLS["m3"]}     - m8:   {MPLUS_ILVLS["m8"]}
- m4:   {MPLUS_ILVLS["m4"]}     - m9:   {MPLUS_ILVLS["m9"]}
- m5:   {MPLUS_ILVLS["m5"]}     - m10:  {MPLUS_ILVLS["m10"]}```"""

dungeons["ilvl_m0"] = f"""The expected ilevel minimum for m0 is {MPLUS_ILVLS["m0"]}"""
dungeons["ilvl_m2-m3"] = f"""The expected ilevel minimum for m2 is {MPLUS_ILVLS["m2"]}, and m3 is {MPLUS_ILVLS["m3"]}"""
dungeons["ilvl_m4-m6"] = f"""The expected ilevel minimum for m4 is {MPLUS_ILVLS["m4"]}, m5 is {MPLUS_ILVLS["m5"]}, and m6 is {MPLUS_ILVLS["m6"]}"""
dungeons["ilvl_m7-m9"] = f"""The expected ilevel minimum for m7 is {MPLUS_ILVLS["m7"]}, m8 is {MPLUS_ILVLS["m8"]} and m9 is {MPLUS_ILVLS["m9"]}"""
dungeons["ilvl_m10"] = f"""The expected ilevel minimum for m10 is {MPLUS_ILVLS["m10"]}.

This is the *maximum* ilvl we allow group creators to set based on the m+ rules in {channel_rules_mplus}, but is also the *minimum* we expect people to be for these dungeons. This is the same ilvl as m9 due to the loot drops being the same, but note that the 9 to 10 key jump has double-scaling due to both the normal 10% key level jump and the introduction of the missing tyrannical or fortified affix so **be prepared** for there to be a big difference in health of mobs and damage taken."""

dungeons["ilvl_channel_addendum"] = "-# - Note that a minimum ilvl is not the only rule when forming mythic plus groups, see `!rules`, or `!mxp` / `!mparty` for details"

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
-# - {general["mods"]}"""

general["newuser_short"] = f"""- {dungeons["lfg"]}
- {raids["join"]}
-# - {general["mods"]}"""
