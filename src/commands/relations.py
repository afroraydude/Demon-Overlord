import discord
import asyncio
import json
import os

# finds relationships one person is in and returns all of them
def check_relationship_single(person, relations):
    keys = relations.keys()

    person_id = person.id

    found_relationships = [] 

    for i in keys:
        if str(person_id) in i: # if the person matches
            found_relationships.append(relations[i]) # it will add that relationship to the list 
        else:
            pass

    if len(found_relationships) == 0: # if no relationships found, return False
        return False
    
    else:
        return found_relationships

            

# this goes through the data to see if a given relationship exists (checked with 2 people)
def check_relationship_spesific(person1, person2, relationship_type, relations): # check if a relationship exists
    keys = relations.keys() # get all relationship names

    people_id1 = person1.id
    people_id2 = person2.id

    people_id = [people_id1, people_id2]
    people_id.sort()

    search = f"{people_id[0]}_{people_id[1]}_{relationship_type}"
    
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
        "person1": person1_id,
        "person2": person2_id,
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
    
    if command[0] != "relation":
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
    mentioned_user = message.mentions[0] #discord.Member version of target_person so we can do actions on him/her



    if command[0] == "break": # if user wants a relationship terminated
        relationship_exists = check_relationship_spesific(message.author, mentioned_user, relation_request["name"] , relations) # use the function above to see if the relationship exists
        if not relationship_exists: # if relationship doesent exist, you cannot terminate it
            await message.channel.send(f'**ERROR - RELATIONSHIP DOESENT EXIST**\nSorry, but you cannot delete a relationship that doesent exist. Thats just sad.')
            return
        
        if relation_request["break"] == "single": # if relationship can be terminated by 1 side 
            remove_relationship(message.author, mentioned_user, relation_request["name"], relations, relation_types_place) # delete dat relationship
            await message.channel.send(f"{author} is no longer {relation_request['usage_name']} with {target_person}!!!")
            return
        
        elif relation_request["break"] == "both": # if relationship requires both sides

            await message.channel.send(f"{author} is asking to no longer be {relation_request['usage_name']} with {target_person} \n He/She must do \"-mao accept\" in 60 seconds order to accept!")

            def check(msg):
                return msg.content == "-mao accept" and msg.author == mentioned_user

            try:
                msg = await bot.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                message.channel.send(f"{target_person} did not accept the request in time. F in the chat for {author}...")
                return
            else:
                remove_relationship(message.author, mentioned_user, relation_request["name"], relations, relation_types_place)
                await message.channel.send(f"{author} is no longer {relation_request['usage_name']} with {target_person}!!!")
                return
        
    elif command[0] == "make": # if user wants to start a relationship
        relationship_exists = check_relationship_spesific(message.author, mentioned_user, relation_request["name"] , relations) # use the function above to see if the relationship exists
        if relationship_exists:
            await message.channel.send(f'**ERROR - RELATIONSHIP ALREADY EXISTS**\nSorry, but that relationship already exists between you 2, please calm down.')
            return
        
        if relation_request["make"] == "single":
            create_relationship(message.author, mentioned_user, relation_request["name"], relations, relation_types_place)
            await message.channel.send(f"{author} is now {relation_request['usage_name']} with {target_person}!!!")

        elif relation_request["make"] == "both":
            
            await message.channel.send(f"{author} is asking to be {relation_request['usage_name']} with {target_person}\n He/She must do \"-mao accept\" in 60 seconds order to accept!")
            
            def check(msg):
                return msg.content == "-mao accept" and msg.author == mentioned_user

            try:
                msg = await bot.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await message.channel.send(f"{target_person} did not accept the request in time. F in the chat for {author}...")
                return
            else:
                create_relationship(message.author, mentioned_user, relation_request["name"], relations, relation_types_place)
                await message.channel.send(f"{author} is now {relation_request['usage_name']} with {target_person}!!!")
                return

    elif command[0] == "relation" and command[1] == "search":
        print("entered relation_search")
        rv = check_relationship_single(mentioned_user, relations)
        
        if not rv and type(rv) is bool:
            await message.channel.send(f"No relationship record has been found of {mentioned_user.display_name}")
            return
        
        if type(rv) is list:
            # prettify the result
            final_message = ""
            for i in rv: # i here is a dictionary consisting both sides uid's and relationship type
                rel_type = i["relationship"] # the relationship type recovered from database
                temp = bot.relation_types[rel_type] # gets the relationship details from relation_types.json
                rel_usg_name = temp["usage_name"] # so that it can get its usage name
                
                person1id = i["person1"]
                person2id = i["person2"]

                if person1id != mentioned_user.id: # if person1 isnt our boyo, that means thats the otherperson
                    otherboyo = bot.get_user(person1id)
                    otherboyoname = otherboyo.display_name

                elif person2id != mentioned_user.id:
                    otherboyo = bot.get_user(person2id)
                    otherboyoname = otherboyo.display_name
                
                final_message += f"{mentioned_user} is {rel_usg_name} with {otherboyoname}.\n"
            
            await message.channel.send(final_message)
            return
        else:
            print("result from relation_search wasnt list of False")

        # okay... i'm sick of all these errors...
    # except Exception as e:
        # await message.channel.send(f"**CHAT - ERROR **\n\nHey {devRole.mention} There was an error.\n```\n{e}\n```")


