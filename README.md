# Discord bot for No Pressure

A `token.toml` file is required, with the following format:
``` yaml
[discord]
token="my_token_from_discord"
bot_id=1234567890
```

For users to use commands they must `@mention` the bot, with commands prefixed by `!` e.g. `@NoP-Bot !help`.

To run the bot navigate to the folder containing the bot, responses, ilvls, and token files and run: 
``` shell
python3 bot.py token.toml
```
The toml files contain:
- `token.toml` contains a discord token for the bot as above
