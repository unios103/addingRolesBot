import discord
import re
from typing import Union


class Help:
    def __init__(self):
        pass

    async def handle(
        self,
        message: discord.Message,
    ):
        file = open("README.md",'r')
        help_text = file.read()
        help_text = help_text.split("##")[1].rstrip("\n\n")
        help_text = "**" + re.sub(r'\n\n', r'**\n', help_text)
        await message.channel.send(help_text)
        file.close()