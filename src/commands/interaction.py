import discord
from . import interactions

async def interactions_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    
    if command[0] == "hug":
        await interactions.hug.handler(bot, message, command, devRole)

    elif command[0] == "blush":
        await interactions.blush.handler(bot, message, command, devRole)

    elif command[0] == "slap":
        await interactions.slap.handler(bot, message, command, devRole)
        
    elif command[0] == "bite":
        await interactions.bite.handler(bot, message, command, devRole)


    elif command[0] == "shrug":
        await interactions.shrug.handler(bot, message, command, devRole)

    elif command[0] == "cry":
        await interactions.cry.handler(bot, message, command, devRole)
    
    elif command[0] == "wave":
        await interactions.wave.handler(bot, message, command, devRole)

    elif command[0] == "pat":
        await interactions.pat.handler(bot, message, command, devRole)
    
    elif command[0] == "shoot":
        await interactions.shoot.handler(bot, message, command, devRole)