import discord
import os


class DemonOverlord(discord.Client):
    async def on_ready(self):

        # change bot's status
        await self.change_presence(activity=discord.Game(name='with fire'))

# START DAT SHIT
bot = DemonOverlord()
bot.run(os.environ['DISCORD_KEY'])
