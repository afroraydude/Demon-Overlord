import discord
import sys, os

# core imports
from DemonOverlord.core.util.config import CommandConfig, BotConfig, DatabaseConfig, APIConfig, RelationshipConfig

class DemonOverlord(discord.Client):

    __slots__ = (
        "config", "commands", "database", "api"
    )

    def __init__(self):
        super().__init__()
        workdir = os.path.dirname(os.path.abspath(__file__))
        confdir = os.path.join(workdir, "../config")

        # set the main bot config
        self.config = BotConfig(confdir, sys.argv)
        self.commands = CommandConfig()
        self.database = DatabaseConfig()
        self.api = APIConfig()
        self.relationships = RelationshipConfig(self.database)

    async def on_ready(self):
        

    async def on_message(self, message:discord.Message):
        pass


bot = DemonOverlord()
bot.run(bot.config.token)