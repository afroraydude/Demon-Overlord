import discord
import os
import misc
import re
import pymongo
import json
import sys

# bot packages
import commands
import extra

# BEHOLD THY LORD
class DemonOverlord(discord.Client):

    async def on_ready(self: discord.Client) -> None:
        print(sys.argv)
        dirname = os.path.dirname(os.path.abspath(__file__))

        # load interactions
        interactions = os.path.join(dirname, 'data/json/interactions.json')
        with open(interactions, "r") as f:
            self.interactions = json.load(f)

        # load relation types
        relation_types = os.path.join(dirname, 'data/json/relation_types.json')
        with open(relation_types, "r") as f: # mother if u reading this thanks for dev role
            self.relation_types = json.load(f)

        # load config
        config = os.path.join(dirname, 'data/json/config.json')
        with open(config, "r") as f:
            self.config = json.load(f)

        # create data dict
        self.data = {}

        #load text files
        for i in self.config["data"].keys():

            # create data
            self.data[i] = {}

            # get all files in subfolder
            for j in self.config["data"][i]:
                path = os.path.join(dirname, f'data/text/{i}/{j}')

                # save data
                with open(path, "r") as f:
                    self.data[i][j] = f.read()


        # get all variables and create DB connection
        dbuser = os.environ["MONGO_USER"]
        dbpass = os.environ["MONGO_PASS"]
        dburl = os.environ["MONGO_URL"]
        mongoUri = f"mongodb+srv://{dbuser}:{dbpass}@{dburl}"


        self.votes = []
        self.izzymojis = {}


        for key in self.config["izzymojis"].keys():
            self.izzymojis[key] = self.get_emoji(self.config["izzymojis"][key])
        

        self.lastCall = {
            "bubbles": [],
            "quote":[]
        }
        # mongo stuff
        #self.mongo = pymongo.MongoClient(mongoUri, port=47410)
        #self.shipdb = self.mongo["demon-overlord"]

        # extra stuff
        tenorkey = os.environ["TENOR_KEY"]
        self.tenor = extra.api.tenor.TenorAPI(tenorkey)

        self.inspirobot = extra.api.inspirobot.InspirobotAPI()
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
        elif self.config == None:
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
        if message.content.startswith(self.config["dev_prefix"] if sys.argv[1] == "--dev" else self.config["prefix"]) and message.author != self:
            await misc.message_handler(self, message)


# START DAT SHIT
bot = DemonOverlord()
bot.run(os.environ['DISCORD_KEY'])
