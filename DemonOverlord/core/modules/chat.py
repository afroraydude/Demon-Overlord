import discord

from DemonOverlord.core.util.responses import TextResponse, BadCommandResponse

async def handler(command) -> discord.Embed:
    chat_list = command.bot.commands.chats

