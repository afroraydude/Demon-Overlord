import discord

from DemonOverlord.core.modules import hello, quote

class Command(object):
    __slots__ = (
        # properties
        "invoked_by", "mentions", "prefix", "command", "action", "params", "bot", "channel", "full"
    )
    def __init__(self, bot:discord.Client, message:discord.message):
        self.invoked_by = message.author
        self.mentions = message.mentions
        self.action = None
        self.bot = bot
        self.channel = message.channel
        self.full = message.content.replace("\n", " ")
        # create the command
        to_filter = ["", " ", None] 
        temp = list( filter( lambda x : not x in to_filter,  message.content.split(" ")))
        self.prefix = temp[0]
        self.command = temp[1]

        # is it a special case?? 
        # WE DO
        if temp[1] in bot.commands.interactions.keys():
            self.action = "interaction"
            self.params = temp[2:] if len(temp) > 2 else None

        # WE LUV 
        elif temp[1] in bot.commands.relations.keys():
            self.action = "relation"
            self.params = temp[2:] if len(temp) > 2 else None
        
        # Y'AIN'T SPECIAL, YA LIL BITCH
        else:
            self.action = temp[1]
            self.params = temp[2:] if len(temp) > 3 else None 
    
    async def exec(self):


        if self.action == "hello":
            response = await hello.handler(self)
        elif self.action == "quote":
            response = await  quote.handler(self)

        await self.channel.send(embed=response)
        
    
    async def rand_status(self):
        pass

    