import discord

from DemonOverlord.core.util.responses import TextResponse, BadCommandResponse

async def handler(command) -> discord.Embed:
    chat_list = command.bot.commands.chats
    chat = "_".join(command.params).lower()
    if chat in chat_list.keys():
        return ChatDescription(command, chat_list[chat])
    else:
        return BadCommandResponse(command)

class ChatDescription(TextResponse):
    def __init__(self, command, chat_desc:dict):
        super().__init__(f'Information about Category - {" ".join(command.params).upper()}', color=0x5d0cb8, icon=command.bot.config.izzymojis["izzyyay"])
        self.chats = chat_desc
        self.timeout = 60
        self.description = f'This is a list of currently available chats in the category `{" ".join(command.params).upper()}`.'
        
        for i in chat_desc:
            self.add_field(
                name = i["name"].upper(),
                value = i["description"],
                inline = False
            )