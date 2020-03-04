import discord


async def handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    if len(message.mentions) == 0:
        return

    mention = message.mentions[0]

    if message.author == mention:
        response = f'{message.author.display_name} waves at themselves'
    else:
        response = f'{message.author.display_name} waves at {mention.display_name}'

    e = discord.Embed(colour=0xff00e7, title=response)
    e.set_image(url=await bot.tenor.get_interact("anime wave"))
    await message.channel.send(embed=e)