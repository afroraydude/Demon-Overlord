import discord

from DemonOverlord.core.modules.interactions.interactions import *

class Command(object):
    __slots__ = (
        # properties
        "invoked_by", "mentions", "prefix", "command", "action", "params", "bot"

        # methods
        "exec", "rand_status"
    )
    def __init__(self, bot:discord.Client, message:discord.message):
        self.invoked_by = message.author
        self.mentions = message.mentions
        
        # create the command
        to_filter = ["", " ", None] 
        temp = list( filter( lambda x : not x in to_filter,  message.split(" ")))
        self.prefix = temp[0]
        self.command = temp[1]

        # is it a special case?? 
        # WE DO
        if self.action in bot.commands.interactions.keys():
            self.action = "interaction"
            self.params = temp[2:] if len(temp) > 2 else None

        # WE LUV 
        elif self.action in bot.commands.relations.keys():
            self.action = "relation"
            self.params = temp[2:] if len(temp) > 2 else None
        
        # Y'AIN'T SPECIAL, YA LIL BITCH
        else:
            self.action = temp[2]
            self.params = temp[3:] if len(temp) > 3 else None 
    
    async def exec(self, bot:discord.Member):
        pass
        
    
    async def rand_status(self):
        pass

    