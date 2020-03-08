import discord

async def bubbles_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    

    try:
        x = int(command[1])
        y = int(command[2])

        # syntax: bubbles {x} {y}
        if (x > 10 or x < 1)  or (y > 10 or y <1):
            response = 'some error'
        else:
            bubbles = "\n".join([" ".join(["||pop||"] * x)]*y)
            response = f'**{bot.izzymojis["Yay"]} BUBBLE WRAP **\n{bubbles}'
        message.channel.send(response)

        bot.lastCall["bubbles"] = None
    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")