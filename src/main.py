import discord
import os
import misc
import re
import commands


# bot config (will later be json)
config = {
    "prefix" : "-mao"
}

class DemonOverlord(discord.Client):

    async def on_ready(self: discord.Client) -> None:
        # save all necessary things in the bot
        self.votes = []

        # change bot's status
        await self.change_presence(activity=await misc.getRandStatus())

    # reaction added to message
    async def on_reaction_add(self, reaction, user):

        # no reacting to own reactions, that'd create WEIRD loops
        if user == self.user:
            return

        # is it a vote, get the title
        title = re.compile("\*\*(.*)\*\*")
        result = list(filter(lambda vote: vote[1]['title'] == title.findall(reaction.message.content)[1] and vote[1]["active"], enumerate(self.votes)))
        
        # well it's not a vote
        if result == None:
            return 

        # OH it's a vote, change the vote count
        elif len(result)>0:
            await commands.voting.vote_edit(bot, reaction, result[0][0], True)

        
    # reaction removed from message
    async def on_reaction_remove(self, reaction, user):
        
        # no reacting to own reactions
        if user == self.user:
            return

        # find the vote
        title = re.compile("\*\*(.*)\*\*")
        result = list(filter(lambda vote: vote[1]['title'] == title.findall(reaction.message.content)[1] and vote[1]["active"], enumerate(self.votes)))

        # NOT A VOTE, let#s do something else
        if result == None:
            return 

        # it's a vote, alright
        elif len(result)>0:
            await commands.voting.vote_edit(bot, reaction, result[0][0], False)
    
    async def on_message(self: discord.Client, message: discord.Message) -> None:
    
        # handle all commands
        if message.content.startswith(config['prefix']) and message.author != self:
            await misc.message_handler(self, message)


# START DAT SHIT
bot = DemonOverlord()
bot.run(os.environ['DISCORD_KEY'])
