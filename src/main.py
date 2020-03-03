import discord
import os
import misc
import re
import commands
import pymongo

# bot config (will later be json)
config = {
    "prefix" : "-mao",
}

# BEHOLD THY LORD
class DemonOverlord(discord.Client):

    async def on_ready(self: discord.Client) -> None:
        # get all variables and create DB connection
        dbuser = os.environ["MONGO_USER"]
        dbpass = os.environ["MONGO_PASS"]
        dburl = os.environ["MONGO_URL"]
        mongoUri = f"mongodb+srv://{dbuser}:{dbpass}@{dburl}"

        # save all necessary things in the bot
        self.votes = []
        self.izzymojis = {
            "izzyangry"  : self.get_emoji(684123588927815710),
            "Yay"        : self.get_emoji(684280248128503855),
            "witchcraft" : self.get_emoji(684135528047968386),
            "izzyblush"  : self.get_emoji(684118795069292552),
            "izzydemon"  : self.get_emoji(684124867024388162),
            "thumbsup"   : self.get_emoji(684127134704205866)
        }

        # mongo stuff
        self.mongo = pymongo.MongoClient(mongoUri, port=47410)
        self.shipdb = self.mongo["demon-overlord"]

        # change bot's status
        await self.change_presence(activity=await misc.getRandStatus())

    # reaction added to message
    async def on_reaction_add(self, reaction, user):

        # no reacting to own reactions, that'd create WEIRD loops
        if user == self.user:
            return

        # is it a vote, get the title
        title = re.compile("\*\*(.*)\*\*")
        if len(self.votes) < 1:
            # this is not the message we're looking for
            return

        result = list(filter(lambda vote:vote[1]['title'] == title.findall(reaction.message.content)[1] and vote[1]["active"], enumerate(self.votes)))
            
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
