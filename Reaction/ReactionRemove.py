import discord
from typing import Union

import Reaction.role_command as rc



class ReactionRemove:
    def __init__(self):
        pass

    async def handle(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        message = reaction.message
        role = rc.get_role(message)

        await user.remove_roles(role)