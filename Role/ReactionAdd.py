import discord
from typing import Union

import Role.role_command as rc



class ReactionAdd:
    def __init__(self):
        pass

    async def handle(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        message = reaction.message
        role = rc.get_role(message)

        await user.add_roles(role)
        await message.channel.send("追加した👾")
