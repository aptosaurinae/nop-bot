# response strings for the bot
try:
   import tomllib
except ModuleNotFoundError:
   import pip._vendor.tomli as tomllib

current_expansion = "tww"
seasons = ["s1", "s2", "s3", "s4"]

ilvls_data = {}
for season in seasons:
    ilvls_file = f"ilvls_{current_expansion}_{season}.toml"
    with open(ilvls_file, "rb") as ilvls_file:
        ilvls_data[season] = tomllib.load(ilvls_file)


channel_channels_and_roles = "<id:customize>"
channel_pick_your_role = "[#pick-your-role](https://discord.com/channels/1055487463734386739/1063229478756696164)"
channel_contact_mods = "[#contact-mods](https://discord.com/channels/1055487463734386739/1063237446042648618)"
channel_guild = "[#nop-guild](https://discord.com/channels/1055487463734386739/1267182548702990377)"
channel_crafting_orders = "[#crafting-orders](https://discord.com/channels/1055487463734386739/1065175223927853107)"

channel_rules_server = "[Server Rules](https://discord.com/channels/1055487463734386739/1180130833487626300)"
channel_rules_mplus = "[additional rules -> Rules for Dungeon Groups](https://discord.com/channels/1055487463734386739/1446127980215537695)"
channel_rules_boiler = "[#boiler-info](https://discord.com/channels/1055487463734386739/1224353705042907187)"

channel_bot_feedback = "[nop-bot feedback thread](https://discord.com/channels/1055487463734386739/1293932439382655098)"

channel_dungeon_get_started = "[Mythic Plus Library](https://discord.com/channels/1055487463734386739/1459209201426370632)"
channel_dungeon_buddy = "[Mythic Plus Library -> Using the M+ Bot](https://discord.com/channels/1055487463734386739/1459210548683079681)"
channel_dungeon_time_complete = channel_rules_mplus

channel_raid_get_started = "[Raiding Library](https://discord.com/channels/1055487463734386739/1459211574672625833)"
channel_raid_leading = "[Raiding Library for Raid Leading](https://discord.com/channels/1055487463734386739/1459214707092361350)"
channel_raid_norm_hero = "[#nm-hc-raids](https://discord.com/channels/1055487463734386739/1065699417342099486)"
channel_raid_mythic = "[#mythic-raids](https://discord.com/channels/1055487463734386739/1224353658926272522)"

channel_lf_mplus = "[#lf-mplus-team](https://discord.com/channels/1055487463734386739/1225099807245467688)"
channel_lf_raid = "[#lf-raid-team](https://discord.com/channels/1055487463734386739/1283124807851839531)"

# ---
help = {}

help["prefix"] = "The following commands are available (prefixed by `!`):"

help["suffix"] = "-# - For more information on individual commands use `!helpall` for a full list in a DM"

help["general"] = f"""general:
- `rules`: a refresher on where you can find various rules
- `roles`: pointers to where roles can be self-assigned
- `guild`: a link to the {channel_guild} channel and some reminders of requirements to join the guild
- `mods`: reminders on how you can contact us
- `addons`: recommended addons for WoW
- `website`: a link to the No Pressure website
- `lfteam`: a link to where to find recruitment resources including the WoW recruitment EU discord
- `newuser`: provides the `rules`, `roles`, `lfg`, and `raidjoin` commands in one
- `newshort`: provides the `lfg`, and `raidjoin` commands in one
- `craft`: provides info on placing crafting orders in NoP
- `communities`: provides a link to the WoWhead discord servers page
- `today`: provides a link to the WoWhead Today in WoW page
- `classic`: provides a link to the Not our Patch discord
- `realms`: Information about picking a realm to play on"""

help["dungeons"] = """dungeons:
- `ilvl`: the guideline ilvls for each m+ difficulty (this adapts depending on which channel it's called in) - requires a season to be provided e.g. `!ilvl s3`
- `mxp`: a reminder of the rule about what experience is expected for keys
- `mparty`: a reminder of the rule about who you can decline from keys
- `lfg`: where you can find instructions on how to join dungeons and use the Dungeon Buddy
- `lfgtemplate`: a template for dungeon groups when not using the buddy
- `affix`: a link to the mythicpl.us website
- `time`: a link to the time / completion etiquette for mythic plus groups"""

help["raids"] = """raids:
- `raidjoin`: where to find information about joining raids
- `raidsetup`: where to find information about setting up raids"""

help["short"] = """- general: `rules`, `roles`, `guild`, `mods`, `addons`, `website`,
`lfteam`, `newuser`, `newshort`, `craft`, `communities`, `today`, `classic`, `realms`
- dungeons: `ilvl <s#>`, `mxp`, `mparty`, `lfg`, `lfgtemplate`, `affix`, `time`
- raids: `raidjoin`, `raidsetup`"""

# ---
general = {}

general["roles"] = f"""You can customise channels and self-assign roles in {channel_channels_and_roles} / {channel_pick_your_role}. Make sure you have emote visibility turned on in the Discord settings."""

general["rules"] = f"""Community wide rules can be found in {channel_rules_server} while m+ specific additions can be found in {channel_rules_mplus} (see {channel_rules_boiler} for high key specific exclusions to these)."""

general["mods"] = f"""Please use {channel_contact_mods} for any non-urgent issues. If you have urgent issues that need immediate resolution then you can ping mods with the `@mods` tag."""

general["guild"] = f"""The NoP guild information can be found in the {channel_guild} channel.
You can only have one character in the guild, and you need to have been a NoP discord member for a week for an application to be accepted.

If you have applied and are waiting for an invite, please note that we are volunteer moderators with a few checks to make for every applicant. We will get to your application but it might take a few days so please be patient."""

general["addons"] = """The recommended addons for use in NoP are:
- `LoggerHead` which allows combat and chat logging automatically on entering specific instances
- `AlterEgo` for tracking m+ and raid progress, and vault completion activities across all your characters
- `WeeklyKnowledge` for tracking profession knowledge across all your characters
- `Warpdeplete` (or similar) to keep track of Mythic Plus dungeon timers and percentages
- `Mythic Dungeon Tools` to plan out routes through dungeons"""

general["website"] = """The NoP website can be found at [no-pressure.eu](https://www.no-pressure.eu)"""

general["lfteam"] = (
    f"You can post personal adverts in {channel_lf_mplus} and {channel_lf_raid} "
    f"(please do not post adverts for your guild here), or if you want to browse guilds "
    f"we recommend the recruitment discord which can be found [here](https://discord.gg/jx8CXHP)\n\n"
    f"-# Your experience on linked Discords is not managed by <No Pressure - EU>. "
    f"<No Pressure - EU> will not be held liable for any interactions, positive or negative, "
    f"you have on other Discord Servers. Linking to an external Discord Server does not "
    f"consitute an endorsement by the <No Pressure - EU> Moderation Team for "
    f"any conduct on such server. Browse at your own risk."
)

general["craft"] = (
    f"You can find crafting orders in {channel_crafting_orders}. "
    f"If you are trying to find someone to do a craft for you, "
    f"**please state your server** as crafts are not region-wide. "
    f"You can check the pins in the channel for a profession sheet "
    f"where you might be able to find a crafter for your realm."""
)

general["communities"] = """If you are playing in other regions or looking for other communities such as class discords try looking at [the WoWhead discord servers page](https://www.wowhead.com/discord-servers)"""

general["today"] = """You can find out what the current things going on in WoW are at the [WoWhead Today in WoW page](https://www.wowhead.com/today-in-wow)"""

general["classic"] = """We are a retail focused discord, and do not currently have any plans to support any of the flavours of classic."""

general["realms"] = """If you are coming from a background playing either classic WoW or many other mmos then the current state of retail might seem weird when it comes to choosing a realm. WoW retail has removed a lot of the walls between things which makes realm choice less of a problem:
- *Faction boundaries*: you can group between horde and alliance, including instanced content; in open world you are in a weird hostile/non-hostile state but can still group together and talk using party chat.
- *Realm boundaries*: you can group with people from other realms, including instanced content, and it will "drag" you into the shard that the group lead is on.
- *Queueable content*: you can queue for content either solo or as a group and end up in groups with players from other realms.
- *Open world*: the open world is "sharded" such that if you are in a particularly low-pop part of the world you're likely to be on the only shard of that area so you'll see pretty much everyone else online in that area regardless of server or faction.
- *PvP vs PvE*: there is no such thing as a PvP or PvE realm any longer. Open world is "default PvE" and there's now a toggle for "war mode" you can turn on in your talents screen in major capitals that makes it so you are effectively in a PvP state in the open world, and you'll only see other people with war mode on.
- *Gold*: You can move money between characters on different realm now using the warbank.

Because of this the realm populations don't matter 99% of the time. There's two elements that are still somewhat realm locked:
- *Crafting*: crafting orders can only be fulfilled by same-realm characters, but even this can be got around as you can craft cross-realm in a guild.
- *Auction house*: Items that don't stack are restricted to the realm, while items that do stack are region wide.

You can find a list of realms with their populations / faction balance here: https://raider.io/realms/eu
"""

# ---
dungeons = {}

for season in seasons:
    mplus_ilvls = ilvls_data[season]["mplus"]
    dungeons[f"ilvl_general_{season}"] = f"""The ilvl guidelines for {season} are:
```- m0:   {mplus_ilvls["m0"]}     - m6:   {mplus_ilvls["m6"]}
- m2:   {mplus_ilvls["m2"]}     - m7:   {mplus_ilvls["m7"]}
- m3:   {mplus_ilvls["m3"]}     - m8:   {mplus_ilvls["m8"]}
- m4:   {mplus_ilvls["m4"]}     - m9:   {mplus_ilvls["m9"]}
- m5:   {mplus_ilvls["m5"]}     - m10:  {mplus_ilvls["m10"]}```"""

    dungeons[f"ilvl_m0_{season}"] = f"""ilvl guideline for {season}: `m0: {mplus_ilvls["m0"]}`."""
    dungeons[f"ilvl_m2-m3_{season}"] = f"""ilvl guidelines for {season}: `m2: {mplus_ilvls["m2"]}`, and `m3: {mplus_ilvls["m3"]}`."""
    dungeons[f"ilvl_m4-m6_{season}"] = f"""ilvl guidelines for {season}: `m4: {mplus_ilvls["m4"]}`, `m5: {mplus_ilvls["m5"]}`, and `m6: {mplus_ilvls["m6"]}`."""
    dungeons[f"ilvl_m7-m9_{season}"] = f"""ilvl guidelines for {season}: `m7: {mplus_ilvls["m7"]}`, `m8: {mplus_ilvls["m8"]}` and `m9: {mplus_ilvls["m9"]}`."""
    dungeons[f"ilvl_m10-m11_{season}"] = f"""ilvl guidelines for {season}: `m10: {mplus_ilvls["m10"]}`."""
    dungeons[f"ilvl_m12-m13_{season}"] = f"""We don't set specific ilvls for this level of key. Note that `m10: {mplus_ilvls["m10"]}` but often keys at this level are more dependent on you knowing the dungeon and your class than explicitly being at a high ilvl."""

dungeons["ilvl_channel_addendum"] = (
    "> This is a **recommended minimum** for character ilvls, but this is also the "
    "**maximum** ilvl threshold we allow group creators to set for rejection.\n"
    "(that is, if your character is above this ilvl then the creator "
    "cannot reject you purely on an ilvl basis).\n"
    "> This is not the only rule for mplus groups: see `!rules`, or `!mxp` / `!mparty` for details"
)

dungeons["xp"] = (
    "Applications to keys where you do not have experience on the level below "
    "the current key level is a perfectly valid reason for a decline and "
    "we recommend you work your way up incrementally 1 level at a time. "
    "Using dungeon score (a.k.a. raider.io / RIO score) is not "
    "a valid reason to decline an applicant, however experience in that specific dungeon is."
)

dungeons["party"] = (
    f"- This is a learning community first and foremost, not a pushing community, "
    f"but part of learning m+ is understanding how to have a balanced composition "
    f"for your group. Declining for party composition is allowed but under the following stipulations:\n"
    f"  - You are fully up-front about the requirements you have.\n"
    f"  - You are asking for something that can be provided by multiple classes.\n"
    f"-# You can get further information at {channel_rules_mplus}"
)

dungeons["lfg"] = (
    f"We recommend you review {channel_dungeon_get_started} before finding dungeon groups in NoP. "
    f"Dungeon Buddy instructions can be found in {channel_dungeon_buddy}."
)

dungeons["time"] = (
    f"If you aren't sure about whether to choose `Time Or Abandon`, "
    f"`Time but Complete` or `Vault Completion` for your key, "
    f"or what to put in the `Timing expectations` section of a template post, "
    f"then see the information in {channel_dungeon_time_complete}. "
    f"Please use `creator_notes` in Dungeon Buddy to set any specific expectations."
)

dungeons["lfgtemplate"] = """When not using Dungeon Buddy, please try and get discord names for each player.
```- `Group Name:`
- `Dungeon & difficulty:`
- `Timing expectations:`
- `Looking for:`
- `Specific Requirements:`
- `Password:` ```
"""

dungeons["affix"] = """You can find the current affix along with lots of other m+ info at the [mythicpl.us website](https://mythicpl.us)"""

# ---
raids = {}

raids["join"] = (
    f"You can find instructions on how to get started with raids in the {channel_raid_get_started}, "
    f"and sign up to raids in {channel_raid_norm_hero} or {channel_raid_mythic}."
)

raids["setup"] = (
    f"We are always looking for more raid organisers! "
    f"You can find instructions on how to set up raids in the {channel_raid_leading}."
)

raids["ilvl"] = (
    "Please see individual raid events for ilvl requirements. "
    "These are typically stated in the description of the event."
)

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
