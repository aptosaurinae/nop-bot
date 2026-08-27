# Discord bot for No Pressure

A `server_info.toml` file is required, with the following format:
``` yaml
token="my_token_from_discord"
bot_name = "NoP-bot-test"
bot_id = 1234567890
server_id = 1234567890
forbidden_role_id = 1234567890

[new_user]
role_id = 1234567890
frequency = 10
file_name = "new_users_test.json"
duration = 30
```

For users to use commands they must `@mention` the bot e.g. `@NoP-Bot !help`.

To run the bot navigate to the folder containing the bot, responses, ilvls, and info files and run: 
``` shell
python3 bot.py server_info.toml
```
