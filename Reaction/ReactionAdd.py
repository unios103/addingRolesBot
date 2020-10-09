import discord
from typing import Union



class ReactionAdd:
    def __init__(self):
        pass

    async def handle(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        await reaction.message.channel.send("test")