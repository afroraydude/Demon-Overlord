import discord
from time import time
from random import randint

async def bubbles_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    # no error handling allowed in here except for the try-except

    try:

        # error handling not found
        if len(command) < 3:
            return

        # set grid size
        x, y = int(command[1]) , int(command[2])
        
        lastcall = list(filter(lambda x : x[1]["user"] == message.author, enumerate(bot.lastCall["bubbles"])))
        print(lastcall)
        # this is not the error you're looking for
        if len(lastcall) > 0:
            print(int(time() - lastcall[0][1]["time"]))
            if int(time() - lastcall[0][1]["time"]) <= 600:
                return
        
        if (x > 10 or x < 1)  or (y > 10 or y <1):
            return
        

        # syntax: bubbles {x} {y}
        # create the bubbles uwu
        else:
            bubbles = "\n".join([" ".join(["||pop||"] * x)]*y)
            posX, posY = randint(0, len(bubbles)) , randint(0, len(bubbles[0]))
            replacements = [
                "||nut||",
                "||owo||"
            ]
            if randint(0,100) % 16 == 0:
                bubbles[posY][posX] = replacements[randint(0,1)]
            response = f'**{bot.izzymojis["Yay"]} BUBBLE WRAP **\n{bubbles}'

            await message.channel.send(response)

            # rate limiter
            if len(lastcall) == 0:
                bot.lastCall["bubbles"].append({
                    "user": message.author,
                    "time": time()
                })
            else:
                bot.lastCall["bubbles"][lastcall[0][0]] = {
                    "user": message.author,
                    "time": time()
                }
        # delete message
        # currently the bot doesn't have the permissions
        #await message.delete()

    # okay... i'm sick of all these errors...
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} HELP - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")