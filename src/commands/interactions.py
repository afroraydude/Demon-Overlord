import discord

class Interaction:
    
    def __init__(self, bot: discord.Client, action: dict, author: str, target: list):
        self.action = action

        if len(target) > 0:
            print(target)
            if author in target and len(target) < 2:
                self.response = f'{author} {action["action"]} themselves'
            elif len(target) > 1:
                self.response = f'{author} {action["action"]} {", ".join(target[:-1])} and {target[-1]}'
            else:
                self.response = f'{author} {action["action"]} {target[0]}'

            self.embed = discord.Embed(colour=0xff00e7, title=self.response)
    
    async def handler(self, bot:discord.Client) -> discord.Embed:
        self.embed.set_image(url=await bot.tenor.get_interact(f'anime {self.action["name"]}'))
        return self.embed

    def set_message(self, message:str) -> None:
        self.embed.add_field(name="Message:", value=message, inline=False)


class AloneInteraction(Interaction):
    def __init__(self, bot: discord.Client, action: dict, author: str):
        super().__init__(bot, action, author, [])

        # generate response
        self.response = f'{author} {action["action"]}'
        self.embed = discord.Embed(colour=0xff00e7, title=self.response)

class SocialInteraction(Interaction):
    def __init__(self, bot: discord.Client, action: dict, author: str, target: list):
        super().__init__(bot, action, author, target)

    
async def interactions_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    try:
        # get all the stuffs
        action = bot.interactions[command[0]]
        author = message.author.display_name
        mentions = [x.display_name for x in message.mentions]

        # frens? 
        if action["type"] == "social":
        
            if len(message.mentions) == 0 and command[1] == "everyone":
                interaction = SocialInteraction(bot, action, author, ["everyone"])
            elif len(message.mentions) > 0:
                interaction = SocialInteraction(bot, action, author, mentions)

            #create a temp array
            temp = " ".join(command[1:]).split(" ")

            # add custom message uwu
            if command[0] == "everyone" and len(temp) > 1:
                interaction.set_message(" ".join(temp[1:]))
            elif len(temp) > len(mentions) and command[0] != "everyone":
                interaction.set_message(" ".join(temp[len(mentions):]))

        # we alone here... 
        elif action["type"] == "alone":
            interaction = AloneInteraction(bot, action, author)

            # add custom message
            if len(command) > 2 + len(mentions):
                interaction.set_message(" ".join(command[1:]))
        
        await message.channel.send(embed=await interaction.handler(bot))

    # okay... i'm sick of all these errors...
    except Exception as e:
       await message.channel.send(f"**{bot.izzymojis['izzyangry']} INTERACTIONS - ERROR **\nHey {devRole.mention} There was an error.\n```\n{e}\n```")