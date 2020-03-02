import discord
import os
import misc


# bot config (will later be json)
config = {
    "prefix" : "-mao"
}

class DemonOverlord(discord.Client):

    async def on_ready(self):
        # change bot's status
        await self.change_presence(activity=await misc.getRandStatus())

    async def on_message(self, message: discord.Message):
    
        # handle all commands
        if message.content.startswith(config['prefix']) and message.author != self:
            await misc.command_handler(self, message)


# START DAT SHIT
bot = DemonOverlord()
bot.run(os.environ['DISCORD_KEY'])
