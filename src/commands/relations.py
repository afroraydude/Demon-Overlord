import discord

def check_relationship(people: list, relationship_type, singe = False): # check if a relationship exists
    if single:

def create_relationship(person1, person2, relationship_type, relations, relation_types_place):
    savename = f"{person1}_{person2}_{relationship_type}"
    relations[savename] = {
        "person1": person1,
        "person2": person2,
        "relationship": relationship_type
    }

    with open(relation_types_place, "r") as f:
        json.dump(relations, f)


def remove_relationship(person1, person2, relationship_type, relations, relation_types_place):

    savename = f"{person1}_{person2}_{relationship_type}"
    del relations[savename]

    with open(relation_types_place, "r") as f:
        json.dump(relations, f)



async def relation_request_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    try:

        dirname = os.path.dirname(os.path.abspath(__file__))
        # import relationships from JSON
        relation_types_place = os.path.join(dirname, 'data/json/relations.json')
        with open(relation_types_place, "r") as f:
            relations = json.load(f)

        # stuff i copied from Dragonsight
        relation_request = bot.relation_types[command[0]]
        author = message.author.displayname
        mentions = [x.display_name for x in message.mentions]

        # a normal relationship command looks like:
        # -moe make/break [relationship type] [person]
        #       idx 0          idx 1            idx 2

        if len(mentions) == 0: # if no mentions made
            await message.channel.send(f'**{bot.izzymojis["izzyangry"]} ERROR - NO TARGET SPECIFIED**\nSorry, but in order to make/break relationship with someone, you need to specify that person. usage: -moe make/break [relationship type] [person]')
            return # be  a n g e r y

        elif len(mentions) > 1: # if tries to make relationships with more than 1 person
            await message.channel.send(f'**{bot.izzymojis["izzyangry"]} ERROR - NO MANY TARGETS**\nSorry, but you can only make/break relationships with 1 person at a time. usage: -moe make/break [relationship type] [person]'
            return

        target_person = mentions[0] # since there is 1 target we dont need a list

        if command[0] is "break": # if user wants a relationship terminated
            if relation_request["break"] == "single": # if break can be executed by one side
                
        elif command[0] is "make": # if user wants to start a relationship

        