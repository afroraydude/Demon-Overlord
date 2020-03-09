import discord

async def chat_handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    if "_".join(command[1]) in bot.data["chat"].keys():
        for i in bot.data["chat"].keys():
            if command[1] == i:
                await message.channel.send(f'**{bot.izzymojis["done"]} CHAT DESCRIPTIONS**\n```asciidoc\n{bot.data["chat"][i]}\n```')
                break
