import discord

from DemonOverlord.core.util.responses import TextResponse

async def handler(command):
    pass

class IzzyLink(TextResponse):
    def __init__(self, command, link:dict):
        super().__init__(f'Izzy - {command.action.upper()}', color=0x784381, icon=command.bot.config.)