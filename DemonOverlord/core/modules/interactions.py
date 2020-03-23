import discord


from DemonOverlord.core.util.responses import ImageResponse


async def handler(command) -> discord.Embed:
    # create shortcuts to make life easier
    alone_interactions = command.bot.commands.interactions["alone"]
    social_interactions = command.bot.commands.interactions["social"]
    music_interactions = command.bot.commands.interactions["music"]

    # what interaction do we have?
    if command.action in alone_interactions.keys():
        return AloneInteractions(command.bot, alone_interactions[command.action], command.invoked_by)
    elif command.action in social_interactions.keys():
        pass
    elif command.action in music_interactions.keys():
        pass

# base interaction


class Interaction(ImageResponse):
    def __init__(self, bot: discord.Client, type: dict, user: discord.Member, title: str = "Interaction", color: int = 0xffffff):
        super().__init__(title, url=bot.api.tenor.get_interact(f'anime {type["query"]}'),
                         color=color, icon=bot.config.izzymojis[type["emoji"]])
        self.type = type
        self.user = user

    def add_message(self, msg: str) -> None:
        self.add_field(name="Message:", value=msg)


# social Interaction
class SocialInteraction(Interaction):
    def __init__(self, type: dict, user: discord.Member, mentions: list):
        super().__init__(type, user, color=0xa251af)


# music interaction, a special case that has both Alone and Social aspects
class MusicInteraction(Interaction):
    def __init__(self, type: dict, user: discord.Member):
        super().__init__(type, user, color=0x1db954)

        spotify = list(filter(lambda x: isinstance(
            x, discord.Spotify), user.activities))
        self.spotify = spotify[0] if len(spotify) > 0 else None

        if self.spotify != None:
            self.add_field(name=self.spotify.title,
                           value=self.spotify.artist, inline=False)


# alone interaction, stuff you do yourself
class AloneInteractions(Interaction):
    def __init__(self, bot: discord.Client, type: dict, user: discord.Member):
        super().__init__(bot, type, user, color=0xe2268f, title=f'{user.display_name} {type["action"]}.')
