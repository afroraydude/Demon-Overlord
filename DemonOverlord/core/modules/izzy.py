import discord

from DemonOverlord.core.util.responses import TextResponse, BadCommandResponse
from DemonOverlord.core.modules.help import HelpCommand

async def handler(command):
    if command.action == None:
        command.action = command.command
        command_help = list(filter(lambda x : x["command"] == command.command, command.bot.commands.list))
        return HelpCommand(command, command_help[0])
    elif command.action in command.bot.commands.izzylinks.keys():
        return IzzyLink(command, command.bot.commands.izzylinks[command.action])
    else:
        return BadCommandResponse(command)

class IzzyLink(TextResponse):
    def __init__(self, command, links:dict):
        super().__init__(f'Izzy - {command.action.replace("_", " ").upper()}', color=0x784381, icon=command.bot.config.izzymojis["izzyyay"])
        print(command.action)
        if command.action != "forbidden_fruit":
            command_obj = list(filter(lambda x : x["command"]=="izzy", command.bot.commands.list))[0]
            action_obj = list(filter(lambda x : x["action"] == command.action, command_obj["actions"]))
            self.description = action_obj[0]["description"]
        else:
            self.timeout = 20
            self.description = "This is the forbidden fruit. Careful, it vanishes."

        for i in links:
            self.add_field(name=i["name"],value=i["link"])
        
