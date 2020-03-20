import discord

async def chat_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:

    try:
        command[3] = command[3].replace(" ", "_")
        category = "_".join(command[1:]).lower()
        categories = "\n".join([f'- {" ".join(x.split("_"))}' for x in bot.data["chat"].keys()])
        print(command)
        # get the descriptions
        if category in bot.data["chat"].keys():
            for i in bot.data["chat"].keys():
                if category == i:
                    response = f'**{bot.izzymojis["done"]} CHAT - {" ".join(command[1:])}**\n```asciidoc\n{bot.data["chat"][i]}\n```'
                    break
        
        # default
        elif not category in bot.data["chat"].keys() and len(command) < 2:
            response = f'**{bot.izzymojis["what"]} CHAT - DESCRIPTIONS**\n\nThis function shows the descriptions for all chats.\nYou can use it like this: `-mao chat {{category}}`\nReplace `{{category}}` with one of the chat caategories.\n```asciidoc\n==== CATEGORIES ====\n{categories}\n```'
        

        else:
            response = f'**{bot.izzymojis["izzyangry"]} CHAT - CATEGORY NOT FOUND**\n\nWhat you entered doesn\'t seem to be a valid category.\nHere is the list of available categories:\n```asciidoc\n==== CATEGORIES ====\n{categories}\n```'

        await message.channel.send(response)
    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} CHAT - ERROR **\n\nHey {devRole.mention} There was an error.\n```\n{e}\n```")
