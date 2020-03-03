import discord

async def izzy_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    
    try:
        # y'aint been givin nuthin, here's all of it
        if len(command) == 1:
            links = [
                "- art     :: instagram accounts",
                "- social  :: any other social media account",
                "- shop    :: all da demonic merch",
                "- website :: The Overlords Website",
                "- support :: Make Sacrifices to the overlord (Kofi and other financial stuff)"
            ]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["izzyblush"]} Links to please The Overlord**\nUse `-mao izzy {{name}}` and replace name with one listed below.`\n```asciidoc\n==== ALL DA LINKS OwO ====\n{linkstr}\n```'

        # all the instagram links
        elif command[1] == "art":
            links = [
                "`The Overlord\'s Art Account` : https://www.instagram.com/theizzypeasy/",
                "`The Overlord\'s Unholy Comics` : https://www.instagram.com/theizzycomics",
            ]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["izzydemon"]} THINE ART SHALL BE SEEN**\n\n{linkstr}'

        # all the social media links
        elif command[1] == "social":
            links = [
                "`Izzy\'s unholy Facebook` : https://www.facebook.com/theizzypeasy",
                "`The Demonic Twitter` : https://twitter.com/theizzypeasy",
                "`Forbidden Tumblr` : https://theizzypeasy.tumblr.com/"
            ]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["thumbsup"]} THEE SHALL BE FAMOUS**\n\n{linkstr}'

        # BUY THA MERCH
        elif command[1] == "shop":
            links = [
                "`INTERNATIONAL GREATNESS FROM IZZY` : http://theizzypeasy.ecwid.com/",
                "`GREATNESS TO THE PHILLIPINES` : https://theizzypeasyph.ecwid.com/"
            ]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["witchcraft"]} WITCHCRAFT CAPITALISM SUPREME - Witchcraft art and accessories by Izzy**\n\n{linkstr}'

        # W E B S I T E
        elif command[1] == "website":
            links = [
                "`ALL DA THINGS` : https://theizzypeasy.carrd.co/"
            ]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["izzydemon"]}'

        # all the financial support
        elif command[1] == "support":
            links = [
                "`Buy a coffee for our overlord` : https://ko-fi.com/theizzypeasy"
            ]
            linkstr = "\n".join(links)
            response = f'**{bot.izzymojis["izzydemon"]} WORLDLY SACRIFICES FOR OUR UNHOLY OVERLORD**\n\n{linkstr}'
        # N O P E
        else:
            response = f'**{bot.izzymojis["izzyangry"]} THY WISH IS NOT MY COMMAND**\n\nSorryyy, but {command[1]} is not a link that exists OwO.'
        await message.channel.send(response)
    # NO NO NO NO, WHY U DO DIS???
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} IZZY**\nHey {devRole.mention} There was an error.\n```\n{e}\n```")