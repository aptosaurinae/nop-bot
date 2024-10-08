# Discord bot for No Pressure

A `token.toml` file is required, with the following format:
``` yaml
[discord]
token="my_token_from_discord"
```


To run the bot navigate to the folder containing the bot and token files and run: 
``` shell
python3 bot.py token.toml channels_test.toml ilvl_tww_s1.toml
```
The toml files contain:
- `token.toml` contains a discord token for the bot as above
- `channels_test.toml` contains a list of channels for the different ! commands for the specific server this is being run on. this has been set up to allow running it on a test server and it pointing to the test channels instead of the "live" channels on the NoP server
- `ilvl_tww_s1.toml` contains a list of itemlevel minimums for the different m+ key levels and raid difficulties for the current season. this is set up to allow easy swapping out of the itemlevels when the next season comes along.
