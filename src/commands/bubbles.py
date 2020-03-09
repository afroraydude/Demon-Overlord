import discord
from time import time

async def bubbles_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    # no error handling allowed in here except for the try-except

    try:

        if len(command) < 3:
            return

        x = int(command[1])
        y = int(command[2])

        if int(time() - bot.lastCall["bubbles"]) < 3000:
            return
        elif (x > 10 or x < 1)  or (y > 10 or y <1):
            return
        

        # syntax: bubbles {x} {y}
        else:
            bubbles = "\n".join([" ".join(["||pop||"] * x)]*y)
            response = f'**{bot.izzymojis["Yay"]} BUBBLE WRAP **\n{bubbles}'
        await message.channel.send(response)

        # no permissions.
        #await message.delete()

        bot.lastCall["bubbles"] = time()
    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")