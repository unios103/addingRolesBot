import discord
import os
from typing import Union

from Reaction.ReactionAdd import ReactionAdd



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        self._reaction_add = ReactionAdd()

    async def on_message(self, message: discord.Message):
        pass

    async def on_reaction_add(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        self._reaction_add.handle(reaction, user)