import discord

from DemonOverlord.core.modules import hello, quote, help, interactions, izzy, chat, vote
from DemonOverlord.core.util.responses import TextResponse, RateLimitResponse, ErrorResponse, BadCommandResponse


class Command(object):

    def __init__(self, bot: discord.Client, message: discord.message):
        self.invoked_by = message.author
        self.mentions = message.mentions
        self.action = None
        self.bot = bot
        self.channel = message.channel
        self.full = message.content.replace("\n", " ")
        self.special = None
        self.message = message

        # create the command
        to_filter = ["", " ", None]
        temp = list(filter(lambda x: not x in to_filter,
                           message.content.split(" ")))
        self.prefix = temp[0]
        self.command = temp[1]

        # is it a special case??
        # WE DO
        if (
            temp[1] in bot.commands.interactions["alone"].keys()
            or temp[1] in bot.commands.interactions["social"].keys()
            or temp[1] in bot.commands.interactions["combine"].keys()
        ):
            self.command = "interactions"
            self.action = temp[1]
            self.special = bot.commands.interactions
            self.params = temp[2:] if len(temp) > 2 else None

        # WE LUV
        elif temp[1] in bot.commands.relations.keys():
            self.action = "relation"
            self.params = temp[2:] if len(temp) > 2 else None
        elif self.command == "chat":
            self.action = None
            self.params = temp[2:] if len(temp) > 2 else None
        # Y'AIN'T SPECIAL, YA LIL BITCH
        else:
            self.action = temp[2] if len(temp) > 2 else None
            self.params = temp[2:] if len(temp) > 3 else None

    async def exec(self) -> None:
        if self.bot.commands.ratelimits.exec(self):

            if self.command == "hello":
                response = await hello.handler(self)
            elif self.command == "quote":
                response = await quote.handler(self)
            elif self.command == "help":
                response = await help.handler(self)
            elif self.command == "interactions":
                response = await interactions.handler(self)
            elif self.command == "izzy":
                response = await izzy.handler(self)
            elif self.command == "chat":
                response = await chat.handler(self)
            elif self.command == "vote":
                response = await vote.handler(self)
            else:
                response = BadCommandResponse(self)
        else:
            # rate limit error
            response = RateLimitResponse(self)
        message = await self.channel.send(embed=response)

        # remove error messages and messages with timeout
        if isinstance(response, (TextResponse)):
            if response.timeout > 0:
                await message.delete(delay=response.timeout)

            if isinstance(response, (ErrorResponse)):

                # send an error meassage to dev channel
                dev_channel = message.guild.get_channel(684100408700043303)
                await dev_channel.send(embed=response)

        await self.message.delete(delay=1)

    async def rand_status(self):
        pass
