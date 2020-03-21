import discord


from  DemonOverlord.core.util.responses import ImageResponse
from DemonOverlord.core.util.api.tenor import TenorAPI

# base interaction
class Interaction(ImageResponse):
    def __init__(self, type:dict, user:discord.Member, color:int=0xffffff):
        super().__init__(title=f'', color=color, )
        self.type = type
        self.user = user


# social Interaction
class SocialInteraction(Interactions):
    def __init__(self, type:dict, user:discord.Member):
        pass

# music interaction, a special case that has both Alone and Social aspects
class MusicInteraction(Interaction):
    def __init__(self, type:dict, user:discord.Member):
        super().__init__(type, user, 0x1db954)

        spotify = list(filter(lambda x : isinstance(x, discord.Spotify), user.activities))
        self.spotify = spotify[0] if len(spotify) > 0 else None
        
        if self.spotify != None:
            self.add_field(name=self.spotify.title, value=self.spotify.artist, inline=False)


        

        
class AloneInteractions(Interaction):
    pass