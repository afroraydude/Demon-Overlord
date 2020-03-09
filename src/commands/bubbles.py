import discord
from time import time

async def bubbles_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    # no error handling allowed in here except for the try-except

    try:

        # error handling not found
        if len(command) < 3:
            return

        # set grid size
        x = int(command[1])
        y = int(command[2])

        # this is not the error you're looking for
        if int(time() - bot.lastCall["bubbles"]) < 300:
            return
        elif (x > 10 or x < 1)  or (y > 10 or y <1):
            return
        

        # syntax: bubbles {x} {y}
        # create the bubbles uwu
        else:
            bubbles = "\n".join([" ".join(["||pop||"] * x)]*y)
            response = f'**{bot.izzymojis["Yay"]} BUBBLE WRAP **\n{bubbles}'

        await message.channel.send(response)

        # delete message
        # currently the bot doesn't have the permissions
        #await message.delete()

        # 
        bot.lastCall["bubbles"][message.author.id]
    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")