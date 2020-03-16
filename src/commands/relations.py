import discord
import json
import os


# this goes through the data to see if a given relationship exists (checked with 2 people)
def check_relationship_spesific(person1, person2, relationship_type, relations): # check if a relationship exists
    keys = relations.keys() # get all relationship names

    people_id1 = person1.id
    people_id2 = person2.id

    search = f"{people_id1}_{people_id2}_{relationship_type}"
    
    for i in keys:
        if search in i:
            return True
        else:
            pass

    return False

def create_relationship(person1, person2, relationship_type, relations, relation_types_place):
    person1_id = person1.id
    person2_id = person2.id

    people_id = [person1_id, person2_id]
    people_id.sort()

    savename = f"{people_id[0]}_{people_id[1]}_{relationship_type}"
    relations[savename] = {
        "person1": person1,
        "person2": person2,
        "relationship": relationship_type
    }

    with open(relation_types_place, "w") as f:
        json.dump(relations, f)


def remove_relationship(person1, person2, relationship_type, relations, relation_types_place):
    person1_id = person1.id
    person2_id = person2.id

    people_id = [person1_id, person2_id]
    people_id.sort()


    savename = f"{people_id[0]}_{people_id[1]}_{relationship_type}"
    del relations[savename]

    with open(relation_types_place, "w") as f:
        json.dump(relations, f)



async def relation_request_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    # try:

    dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    # import relationships from JSON
    relation_types_place = os.path.join(dirname, 'data/json/relations.json')
    with open(relation_types_place, "r") as f:
        relations = json.load(f)

    # stuff i copied from Dragonsight
    relation_request = bot.relation_types[command[1]]
    author = message.author.display_name
    mentions = [x.display_name for x in message.mentions]

    # a normal relationship command looks like:
    # -moe make/break [relationship type] [person]
    #       idx 0          idx 1            idx 2

    if len(mentions) == 0: # if no mentions made
        await message.channel.send(f'**ERROR - NO TARGET SPECIFIED**\nSorry, but in order to make/break relationship with someone, you need to specify that person. usage: -moe make/break [relationship type] [person]')
        return # be  a n g e r y

    elif len(mentions) > 1: # if tries to make relationships with more than 1 person
        await message.channel.send(f'**ERROR - TOO MANY TARGETS**\nSorry, but you can only make/break relationships with 1 person at a time. usage: -moe make/break [relationship type] [person]')
        return

    target_person = mentions[0] # since there is 1 target we dont need a list
    mention_id = message.mentions[0]

    relationship_exists = check_relationship_spesific(message.author, mention_id, relation_request["name"] , relations) # use the function above to see if the relationship exists

    if command[0] == "break": # if user wants a relationship terminated
        if not relationship_exists: # if relationship doesent exist, you cannot terminate it
            await message.channel.send(f'**ERROR - RELATIONSHIP DOESENT EXIST**\nSorry, but you cannot delete a relationship that doesent exist. Thats just sad.')
            return
        
        if relation_request["break"] == "single": # if relationship can be terminated by 1 side 
            remove_relationship(message.author, mention_id, relation_request["name"], relations, relation_types_place) # delete dat relationship
            await message.channel.send(f"{author} is no longer {relation_request['usage_name']} with {target_person}!!!")
            return
        
        elif relation_request["break"] == "both": # if relationship requires both sides

            await message.channel.send(f"{author} is asking to no longer be {relation_request['usage_name']} with {target_person} \n He/She must do \"-mao accept\" in 60 seconds order to accept!")

            def check(msg):
                return msg.content == "-mao accept" and msg.author == mention_id

            try:
                msg = await bot.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                message.channel.send(f"{target_person} did not accept the request in time. F in the chat for {author}...")
                return
            else:
                remove_relationship(message.author, mention_id, relation_request["name"], relations, relation_types_place)
                await message.channel.send(f"{author} is no longer {relation_request['usage_name']} with {target_person}!!!")
                return
        
    elif command[0] == "make": # if user wants to start a relationship
        if relationship_exists:
            await message.channel.send(f'**ERROR - RELATIONSHIP ALREADY EXISTS**\nSorry, but that relationship already exists between you 2, please calm down.')
            return
        
        if relation_request["make"] == "single":
            create_relationship(message.author, mention_id, relation_request["name"], relations, relation_types_place)
            await message.channel.send(f"{author} is now {relation_request['usage_name']} with {target_person}!!!")

        elif relation_request["make"] == "both":
            
            await message.channel.send(f"{author} is asking to be {relation_request['usage_name']} with {target_person}\n He/She must do \"-mao accept\" in 60 seconds order to accept!")
            
            def check(msg):
                return msg.content == "-mao accept" and msg.author == mention_id

            try:
                msg = await bot.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                message.channel.send(f"{target_person} did not accept the request in time. F in the chat for {author}...")
                return
            else:
                create_relationship(message.author, mention_id, relation_request["name"], relations, relation_types_place)
                await message.channel.send(f"{author} is now {relation_request['usage_name']} with {target_person}!!!")
                return
        # okay... i'm sick of all these errors...
    # except Exception as e:
        # await message.channel.send(f"**CHAT - ERROR **\n\nHey {devRole.mention} There was an error.\n```\n{e}\n```")


