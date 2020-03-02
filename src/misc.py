# libraries
import discord
from random import randint 

# custom packages
import commands


async def command_handler(bot:discord.User, message:discord.Message) -> None:
    # Assume command structure
    temp = list(filter( lambda x : x != "" and x != " ", message.content.lstrip("-mao ").split(" ")))
    command = temp[0:2] + [" ".join(temp[2:])]

    if command[0] == "hello":
        await message.channel.send(f'**:hibiscus: Hello**\nHello, {message.author.mention}!')
    if command[0] == "ship":
        pass

    
    # 20% chance to change presence
    change = randint(1, 100) % 5
    print(change)
    if change == 0:
        await bot.change_presence(activity=await getRandStatus())
    
    
async def getRandStatus() -> discord.Activity: 

    # activity types:
    # -1 : unknown
    # 0  : playing
    # 1  : streaming
    # 2  : listening
    # 3  : watching

    # set placeholder vars
    listening = discord.ActivityType(2)
    watching = discord.ActivityType(3)

    # the list of all possible statuses
    statusList = [
        # playing ... 
        discord.Game(name='with fire'),      # playing with fire
        discord.Game(name='with blood'),     # playing with blood
        discord.Game(name='with Izzy'),      # playing with Izzy
        discord.Game(name='with my minions'),

        # streaming ...
        discord.Streaming(name="the Summoning"),
        

        # listening to ...
        discord.Activity(name="screams of the damned", type=listening),      # listening to 

        # watching ...
        discord.Activity(name="the guilty burn", type=watching)             # watching the guilty burn

    ]

    # select one and return
    index = randint(0, len(statusList)-1)
    print(index)
    return statusList[index]