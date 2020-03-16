# libraries
import discord
from random import randint 

# custom packages
import commands


async def message_handler(bot:discord.Client, message:discord.Message) -> None:
    devRole = discord.utils.get(message.guild.roles, name="Dev-Demons")

    # Assume command structure
    temp = list(filter( lambda x : x != "" and x != " ", message.content.lstrip("-mao ").split(" ")))
    command = list(filter(lambda x : x != "" and x != " ", temp[0:2] + [" ".join(temp[2:])]))
    
    # handle hello 
    if command[0] == "hello":
        await message.channel.send(f'**:hibiscus: Hello**\nHello, {message.author.mention}!')

    # handle help
    elif command[0] == "help":
        await commands.help.help_handler(bot, message, command, devRole)
    
    # vote handler
    elif command[0] == "vote":
        await commands.voting.vote_handler(bot, message, command, devRole)
    
    # handle izzy UwU 
    elif command[0] == "izzy":
        await commands.izzy.izzy_handler(bot, message, command, devRole)
    
    # handle ship
    elif command[0] == "ship":
        pass
    
    # handle bubbles OwO
    elif command[0] == "bubbles":
        await commands.bubbles.bubbles_handler(bot, message, command, devRole)
    
    # chat descriptions
    elif command[0] == "chat":
        await commands.chat.chat_handler(bot, message, command, devRole)

    elif command[0] == "lmgtfy":
        await commands.lmgtfy.lmgtfy_handler(bot, message, command, devRole)
        
    # handle all interactions
    elif command[0] in bot.interactions.keys():
        await commands.interactions.interactions_handler(bot, message, command, devRole)

    # handle all relation requests
    elif command[0] == in bot.relation_types.keys():
        await commands.relations.relation_request_handler(bot, message, command, devRole)
    
    # 20% chance to change presence
    change = randint(1, 100) % 5
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
        discord.Streaming(name="the Summoning", url="https://www.instagram.com/theizzycomics/"),  # links to izzy's insta :p
        discord.Streaming(name="Izzy Merch", url="http://theizzypeasy.ecwid.com/"),

        # listening to ...
        discord.Activity(name="screams of the damned", type=listening),      # listening to 

        # watching ...
        discord.Activity(name="the guilty burn", type=watching)             # watching the guilty burn

    ]

    # select one and return
    index = randint(0, len(statusList)-1)
    return statusList[index]
