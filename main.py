import discord
import os
from typing import Union

from Role.ReactionAdd import ReactionAdd
from Role.ReactionRemove import ReactionRemove
from Help.Help import Help


class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        self._reaction_add = ReactionAdd()
        self._reaction_remove = ReactionRemove()
        self._help_command = Help()

    async def on_message(self, message: discord.Message):
        pass

    async def on_reaction_add(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        if user.bot:
            return

        await self._reaction_add.handle(reaction, user)

    async def on_reaction_remove(
        self,
        reaction: discord.Reaction,
        user: Union[discord.Member, discord.User]
    ):
        if user.bot:
            return

        await self._reaction_remove.handle(reaction, user)

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if message.content == "+help":
            await self._help_command.handle(message)


if __name__ == "__main__":
    client = Client()
    client.run()