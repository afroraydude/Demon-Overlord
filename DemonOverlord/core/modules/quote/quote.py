import discord

from DemonOverlord.core.util.responses import ImageResponse
from DemonOverlord.core.util.api.inspirobot import InspirobotAPI
class Quote(ImageResponse):
    def __init__(self):
        super().__init__("Quote from Inspirobot", InspirobotAPI().get_quote())

