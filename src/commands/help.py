import discord
from . import interactions
# handle help requests


async def help_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    try:
        # get the help page from config
        if command[1] in bot.config["help"].keys():
            comm = "\n".join(bot.config["help"][command[1]])
        
        # main help
        if len(command) < 2 or command[1] == "":
            response = f"**:grey_question: HELP**\nThis is a list of currently available commands.\nTo use a command, write `-mao {{command}} {{action}} {{arguments}}`.\nTo get more information about actions and their arguments, write `-mao help {{command}}`.\n```asciidoc\n{comm}\n```"

        # get all the different Help pages
        else:
            
            # REALLY???
            if command[1] == "help":
                response = f"**:grey_question: HELP**\nThis is a list of currently available commands.\nTo use a command, write `-mao {{command}} {{action}} {{arguments}}`.\nTo get more information about actions and their arguments, write `-mao help {{command}}`.\n```asciidoc\n{comm}\n```"

            # WE LOVE DEMOCRACY
            elif command[1] == "vote":
                response = f"**:grey_question: HELP    --    vote **\nThis is a list of actions and their parameters. To use them, write `-mao vote {{action}} {{arguments}}`.\n```asciidoc\n===== ACTIONS =====\n{comm}\n```"

            # WE LOVE IZZY
            elif command[1] == "izzy":
                response = f'**:grey_question: HELP    --    izzy **\nThis command can give you all the links to look at or buy Izzy stuff.\nUse `-mao izzy {{name}}` and replace name with one listed below.`\n```asciidoc\n==== ALL DA LINKS OwO ====\n{comm}\n```'
            
            # HUGGIEEES
            elif command[1] == "interactions":
                response = f"**:grey_question: HELP    --    interactions **\nThis is a list of interactions. To use them, write `-mao {{action}} {{target}} {{custom message}}`\n\n`{{custom message}}` is optional.\n`{{target}}`can be one of two things:\n```asciidoc\n1 :: a list of @ mentions\n2 :: 'everryone'\n```\n\nHre is a list of currently available interactions. Actions in `ALONE ONLY` don't use the @mention, you do that alone.\n```asciidoc\n===== ACTIONS =====\n{comm}\n```"
            
            # that doesn't seem to exist...
            else:
                response = f"**{bot.izzymojis['izzyangry']} HELP - NONEXISTENT COMMAND **\n THAT is not a command currently supported.\n You can add a request with `$feature add {{text}}` or list the available commands with `$help`"

        # respond to the minions
        await message.channel.send(response)

    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")