import discord

from DemonOverlord.core.util.responses import TextResponse

async def handler(command) -> discord.Embed:
    msg = {
        "name": 'Response:',
        "value": f'Hello, {command.invoked_by.mention}'
    }
    res = TextResponse("Command - Hello", color=0xef1dd9, icon=command.bot.config.izzymojis["hello"] or "🌺", msg=msg)
    return res