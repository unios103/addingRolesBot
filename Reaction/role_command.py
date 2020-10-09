import discord
from typing import Optional



def get_role(message: discord.Message) -> Optional[discord.Role]:
    words = message.content.split()

    if len(words) < 2:
        return None

    if words[0] != "+role":
        return None

    return message.guild.get_role(int(words[1][3: -1]))