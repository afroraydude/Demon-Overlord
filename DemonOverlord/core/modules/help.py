import discord

from DemonOverlord.core.util.responses import TextResponse, BadCommandResponse


async def handler(command) -> discord.Embed:
    if command.action is None or command.action == "help":
        return HelpMain(command, command.bot.commands.help)
    if command.action in command.bot.commands.help:
        return HelpCommandCategory(command, command.bot.commands.help[command.action])
    else:
        return BadCommandResponse(command)



# each normal command only gets this.
class HelpCommandCategory(TextResponse):
    def __init__(self, command, help_dict: dict):
        super().__init__(f'Help - {command.action}', color=0x2cd5c9, icon='❓')
        self.help = help_dict
        self.timeout = self.help["timeout"]
        self.syntax = f'`{command.bot.config.mode["prefix"]} {self.help["command_syntax"]}`'
        self.description = self.help["description"]
        self.actions = None

        # add the action list
        self.actions = ""
        for i in self.help["actions"]:
            self.actions += f'{i["action"]}\n'

        # add all the necessary fields
        self.add_field(name='Description',
                       value=self.description, inline=False)
        self.add_field(name='Command usage:',
                       value=self.syntax, inline=False)
        self.add_field(name='Available Commands:',
                       value=f'```asciidoc\n{self.actions}\n```', inline=False)

class HelpMain(HelpCommandCategory):
    def __init__(self, command, help_dict:dict):
        command.action = "Main"
        super().__init__(command, help_dict["help"])
        self.main_syntax = f'`{command.bot.config.mode["prefix"]} {{command}} {{action}} {{parameters}}`'

        # add the category string
        self.categories = ""
        for i in self.help["categories"]:
            self.categories += f'{i["action"]}\n'

        # add all the necessary fields
        self.insert_field_at(1,name='General Command Syntax:',
                       value=self.main_syntax, inline=False)
        self.add_field(name='Available Categories:',
                       value=f'```asciidoc\n{self.categories}\n```', inline=False)

class HelpCommand(TextResponse):
    def __init__(self, command, help_dict: dict):
        #super().__init__(title, color=color, icon=icon, msg=msg)
        pass
