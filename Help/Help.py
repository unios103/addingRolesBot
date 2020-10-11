import discord
import re
from typing import Union


class Help:
    def __init__(self):
        file = open("README.md",'r',encoding="utf-8")
        help_text = file.read()
        help_text = help_text[re.search(r'## コマンド', help_text).end():].split("## ")[0].strip()
        self._help_text = "***📝 コマンド一覧***\n" + help_text
        file.close()

    async def handle(
        self,
        message: discord.Message,
    ):
        await message.channel.send(self._help_text)