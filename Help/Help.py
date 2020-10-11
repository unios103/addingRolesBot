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
        help_text = help_text[re.search(r'## コマンド', help_text).end():].split("## ")[0].strip()
        help_text = "***📝 コマンド一覧***\n" + help_text
        await message.channel.send(help_text)
        file.close()