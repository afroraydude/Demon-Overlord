import discord
from . import interactions
# handle help requests


async def help_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    try:
        # get the help page from config
        if len(command) > 1 and command[1] in bot.config["help"].keys():
            comm = "\n".join(bot.config["help"][command[1]])
        else:
            comm = "\n".join(bot.config["help"]["help"])
        
        # main help
        if len(command) < 2 or command[1] == "":
            response = f"**{bot.izzymojis['what']} HELP**\n\nTo use a command, write `-mao {{command}} {{action}} {{arguments}}`.\nTo get more information about actions and their arguments, write `-mao help {{command}}`.\n\n__Here is a list of all currently available commands:__\n```asciidoc\n{comm}\n```"

        # get all the different Help pages
        else:
            
            if command[1] == "hello":
                return
            
            # REALLY???
            elif command[1] == "help":
                response = f"**{bot.izzymojis['what']} HELP**\n\nTo use a command, write `-mao {{command}} {{action}} {{arguments}}`.\nTo get more information about actions and their arguments, write `-mao help {{command}}`.\n\n__Here is a list of all currently available commands:__\n```asciidoc\n{comm}\n```"

            # WE LOVE DEMOCRACY
            elif command[1] == "vote":
                response = f"**{bot.izzymojis['what']} HELP    --    vote **\n\nThis is a list of actions and their parameters. To use them, write `-mao vote {{action}} {{arguments}}`.\n```asciidoc\n{comm}\n```"
            
            # WE LOVE DEMOCRACY
            elif command[1] == "lmgtfy":
                response = f"**{bot.izzymojis['what']} HELP    --    lmgtfy **\n\nA command to give answers to that one person that asked you instead of just looking it up.\nUsage:`-mao lmgtfy {{search query}}`"

            # WE LOVE IZZY
            elif command[1] == "izzy":
                response = f'**{bot.izzymojis["what"]} HELP    --    izzy **\n\nThis command can give you all the links to look at or buy Izzy stuff.\nUse `-mao izzy {{name}}` and replace name with one listed below.`\n```asciidoc\n==== ALL DA LINKS OwO ====\n{comm}\n```'
            
            # HUGGIEEES
            elif command[1] == "interactions":
                response = f"**{bot.izzymojis['what']} HELP    --    interactions **\n\nTo use this command, write `-mao {{action}} {{target}} {{custom message}}`\n\n`{{custom message}}` is optional.\n`{{target}}`can be one of two things:\n```asciidoc\n1 :: a list of @ mentions\n2 :: 'everyone'\n```\n\nHere is a list of currently available interactions. Actions in `ALONE ONLY` don't use the @mention, you do that alone.\n```asciidoc\n{comm}\n```"
            
            elif command[1] == "chat":
                categories = "\n".join([f'- {" ".join(x.split("_"))}' for x in bot.data["chat"].keys()])
                response = f'**{bot.izzymojis["what"]} CHAT - DESCRIPTIONS**\n\nThis function shows the descriptions for all chats.\nYou can use it like this: `-mao chat {{category}}`\nReplace `{{category}}` with one of the chat caategories.\n```asciidoc\n==== CATEGORIES ====\n{categories}\n```'
            # that doesn't seem to exist...
            else:
                response = f"**{bot.izzymojis['izzyangry']} HELP - NONEXISTENT COMMAND **\n\nTHAT is not a command currently supported.\n You can add list the available commands with `-mao help`"

        # respond to the minions
        await message.channel.send(response)

    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\n\nHey {devRole.mention} There was an error.\n```\n{e}\n```")