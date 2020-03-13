import discord

async def izzy_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    
    try:
        # y'aint been givin nuthin, here's all of it
        if len(command) == 1:
            links = bot.config["help"]["izzy"]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["izzyblush"]} Links to please The Overlord**\nUse `-mao izzy {{name}}` and replace name with one listed below.`\n```asciidoc\n==== ALL DA LINKS OwO ====\n{linkstr}\n```'

        else:
            if command[1] in bot.config["izzylinks"]:
                linkstr = "\n".join(bot.config["izzylinks"][command[1]])
            else:
                return

            # all the instagram links
            if command[1] == "art":
                response = f'**{bot.izzymojis["izzydemon"]} THINE ART SHALL BE SEEN**\n\n{linkstr}'

            # all the social media links
            elif command[1] == "social":
                response = f'**{bot.izzymojis["thumbsup"]} THEE SHALL BE FAMOUS**\n\n{linkstr}'

            # BUY THA MERCH
            elif command[1] == "shop":
                response = f'**{bot.izzymojis["witchcraft"]} WITCHCRAFT CAPITALISM SUPREME - Witchcraft art and accessories by Izzy**\n\n{linkstr}'

            # W E B S I T E
            elif command[1] == "website":
                response = f'**{bot.izzymojis["izzydemon"]} THE GREAT WEBSITE OF OUR LEADER**\n\n{linkstr}'

            # all the financial support
            elif command[1] == "support":
                response = f'**{bot.izzymojis["izzydemon"]} WORLDLY SACRIFICES FOR OUR UNHOLY OVERLORD**\n\n{linkstr}'
            elif command[1] == "stickers":
                response = f'**{bot.izzymojis["izzydemon"]} ALL DA STICKERS**\n\n{linkstr}'
            # N O P E
            else:
                response = f'**{bot.izzymojis["izzyangry"]} THY WISH IS NOT MY COMMAND**\n\nSorryyy, but {command[1]} is not a link that exists OwO.'
        await message.channel.send(response)
    # NO NO NO NO, WHY U DO DIS???
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} IZZY**\nHey {devRole.mention} There was an error.\n```\n{e}\n```")