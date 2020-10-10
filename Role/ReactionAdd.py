import discord
from typing import Union

import Role.role_command as rc
import Role.corresponding_role as cr


class ReactionAdd:
    def __init__(self):
        pass

    async def handle(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        message = reaction.message
        role = cr.get_corresponding_role(message, reaction.emoji)

        if role == None:
            return

        await user.add_roles(role)
        await message.channel.send(str(user.name) + " に " +str(role) + " を追加した👾")
