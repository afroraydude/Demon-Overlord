import discord

class RelationRequest:

    def __init__(self, bot: discord.Client, relation_request: dict, author: str, target: list):
        self.relation_request = relation_request 

        if len(target) > 1

async def relation_request_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    relation_request = bot.relation_types[command[0]]
    author = message.author.displayname
    mentions = [x.display_name for x in message.mentions]

    