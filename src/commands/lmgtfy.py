import discord

async def lmgtfy_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role):
    try:
        if len(command) >1:
            lookup = " ".join(command[1:]).replace(" ", "%20")
            google_icon = 'https://maxcdn.icons8.com/Share/icon/Logos/google_logo1600.png'
            query_url = f'http://lmgtfy.com/?q={lookup}'
            response = discord.Embed(color=0xF9F9F9)
            response.set_author(name='Click here to go to the results.', icon_url=google_icon, url=query_url)
            await message.channel.send(embed=response)
        else:
            response = f'**{bot.izzymojis["angryizzy"]}**\nThis Function is for when you have that one person that asks you something they could easily look up. Usage: `-mao lmgtfy {{search}}`'
            await message.channel.send(response)
        
    # NO NO NO NO, WHY U DO DIS???
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} IZZY**\nHey {devRole.mention} There was an error.\n```\n{e}\n```")