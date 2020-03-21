import discord
import sys, os

# core imports
from DemonOverlord.core.util.config import CommandConfig, BotConfig

class DemonOverlord(discord.Client):

    __slots__ = (
        "config", "commands"
    )

    def __init__(self):
        super().__init__()
        workdir = os.path.dirname(os.path.abspath(__file__))
        confdir = os.path.join(workdir, "../config")
        self.config = BotConfig(confdir)
        self.commands = CommandConfig()

    async def on_message(self, message:discord.Message):
        pass


bot = DemonOverlord()
bot.run(bot.config.token)