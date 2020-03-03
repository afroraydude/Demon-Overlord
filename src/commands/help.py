import discord

# handle help requests
async def help_handler(bot: discord.Client, message: discord.Message, command: list, devRole:discord.Role) -> None:
    
    try:
        # main help
        if len(command) < 2 or command[1] == "":
            response = await help_main()

        # get all the different Help pages
        else:
            # WE LOVE DEMOCRACY
            if command[1] == "vote":
                response = await voting()
                
            # that doesn't seem to exist...
            else:
                response = "**:x: HELP - NONEXISTENT COMMAND **\n THAT is not a command currently supported.\n You can add a request with `$feature add {text}` or list the available commands with `$help`"
        await message.channel.send(response)

    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**:x: HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")


# main help
async def help_main() -> str:
    cList = [
        "- help     ::   sends this message",
        "- hello    ::   says hello to the sender (has no special action)",
        "- vote     ::   creates, removes or lists active votes"
    ]

    comm = ""
    for i in cList:
        comm += i + "\n"
    response = f"**:grey_question: HELP**\nThis is a list of currently available commands.\nTo use a command, write `-mao {{command}} {{action}} {{arguments}}`.\nTo get more information about actions and their arguments, write `$help {{command}}`.\n```asciidoc\n==== COMMANDS ====\n{comm}\n```"

    return response

# help for vote command
async def voting() -> str:
    alist = [
        "- list                       :: list all currently active votes",
        "- create {name};{options}    :: creates a vote  with name {name} and all options separated by comma",
        "- end {name}                 :: removes the active quote with name {name}"
    ]
    comm = ""
    for i in alist:
        comm += i + "\n"
    response = f"**:grey_question: HELP    --    vote **\nThis is a list of actions and their parameters. To use them, write `$vote {{action}} {{arguments}}`.\n```asciidoc\n===== ACTIONS =====\n{comm}\n```"
    return response