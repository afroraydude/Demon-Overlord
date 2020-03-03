import discord

async def izzy_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    
    try:
        pass
    # NO NO NO NO, WHY U DO DIS???
    except Exception as e:
        await message.channel.send(f"**:x: IZZY**\nHey {devRole.mention} There was an error.\n```\n{e}\n```")