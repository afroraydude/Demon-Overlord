import discord

from DemonOverlord.core.modules import hello, quote, interactions
from DemonOverlord.core.util.responses import RateLimitResponse, ErrorResponse


class Command(object):
    __slots__ = (
        # properties
        "invoked_by", "mentions", "prefix", "command", "action", "params", "bot", "channel", "full", "special", "message"
    )

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
        if temp[1] in bot.commands.interactions["alone"].keys() or temp[1] in bot.commands.interactions["social"].keys() or temp[1] in bot.commands.interactions["music"].keys():
            self.action = "interaction"
            self.special = bot.commands.interactions
            self.params = temp[2:] if len(temp) > 2 else None

        # WE LUV
        elif temp[1] in bot.commands.relations.keys():
            self.action = "relation"
            self.params = temp[2:] if len(temp) > 2 else None

        # Y'AIN'T SPECIAL, YA LIL BITCH
        else:
            self.action = temp[1]
            self.params = temp[2:] if len(temp) > 3 else None

    async def exec(self) -> None:

        if self.bot.commands.ratelimits.exec(self):

            if self.action == "hello":
                response = await hello.handler(self)
            elif self.action == "quote":
                response = await quote.handler(self)
            elif self.action == "interactions":
                response = interactions.handler(self)
        else:
            # rate limit error
            response = RateLimitResponse(self)

        message = await self.channel.send(embed=response)

        # remove traces
        if isinstance(response, (RateLimitResponse, ErrorResponse)):
            await message.delete(delay=10)

            if isinstance(response, (ErrorResponse)):

                # send an error meassage to dev channel
                dev_channel = message.guild.get_channel(684100408700043303)
                await dev_channel.send(embed=response)

        await self.message.delete(delay=1)

    async def rand_status(self):
        pass
