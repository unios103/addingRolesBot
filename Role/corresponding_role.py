import discord
import re
from typing import Optional

import Role.role_command as rc

def get_corresponding_role(message: discord.Message, emoji: discord.Emoji) -> Optional[discord.Role]:
    contents = re.sub(r'( |\n)', '', message.content)

    command_search = re.search(r'\+role', contents)
    if command_search == None:
        return None

    contents = contents[command_search.end():]

    if contents.find("=") == -1:
        return rc.get_role(message)

    match_emoji = contents.find(str(emoji))
    if match_emoji == -1:
        return None

    role = contents[match_emoji:].split(",")[0].split("=")[1][3: -1]

    return message.guild.get_role(int(role))