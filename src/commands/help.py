import discord

# handle help requests


async def help_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    try:
        # main help
        if len(command) < 2 or command[1] == "":
            response = await help_main()

        # get all the different Help pages
        else:
            # REALLY???
            if command[1] == "help":
                response = await help_main()

            # WE LOVE DEMOCRACY
            elif command[1] == "vote":
                response = await voting()

            # WE LOVE IZZY
            elif command[1] == "izzy":
                response = await izzy()

            # that doesn't seem to exist...
            else:
                response = f"**{bot.izzymojis['izzyangry']} HELP - NONEXISTENT COMMAND **\n THAT is not a command currently supported.\n You can add a request with `$feature add {{text}}` or list the available commands with `$help`"

        # respond to the minions
        await message.channel.send(response)

    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")


# main help
async def help_main() -> str:
    cList = [
        "- help     ::   sends this message",
        "- hello    ::   says hello to the sender (has no special action)",
        "- vote     ::   creates, removes or lists active votes",
        "- izzy     ::   all things Izzy"
    ]

    comm = "\n".join(cList)
    response = f"**:grey_question: HELP**\nThis is a list of currently available commands.\nTo use a command, write `-mao {{command}} {{action}} {{arguments}}`.\nTo get more information about actions and their arguments, write `$help {{command}}`.\n```asciidoc\n==== COMMANDS ====\n{comm}\n```"

    return response


# help for vote command
async def voting() -> str:
    alist = [
        "- list                       :: list all currently active votes",
        "- create {name};{options}    :: creates a vote  with name {name} and all options separated by comma",
        "- end {name}                 :: removes the active quote with name {name}"
    ]
    comm = "\n".join(alist)
    response = f"**:grey_question: HELP    --    vote **\nThis is a list of actions and their parameters. To use them, write `$vote {{action}} {{arguments}}`.\n```asciidoc\n===== ACTIONS =====\n{comm}\n```"
    return response


# handle the impossible
async def izzy() -> str:
    links = [
        "- art     :: instagram accounts",
        "- social  :: any other social media account",
        "- shop    :: all da demonic merch",
        "- website :: The Overlords Website",
        "- support :: Make Sacrifices to the overlord (Kofi and other financial stuff)"
    ]
    linkstr = "\n".join(links)
    response = f'**:grey_question: HELP    --    vote **\nThis command can give you all the links to look at or buy Izzy stuff.\nUse `-mao izzy {{name}}` and replace name with one listed below.`\n```asciidoc\n==== ALL DA LINKS OwO ====\n{linkstr}\n```'
