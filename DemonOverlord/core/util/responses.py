import discord

from DemonOverlord.core.util.command import Command


class TextResponse(discord.Embed):
    def __init__(self, title: str, color: int = 0xffffff, icon: str = "", msg: dict = None):
        super().__init__(title=f'{icon} {title}', color=color)

        if msg != None:
            self.add_field(name=msg["name"], value=msg["value"])


class ErrorResponse(TextResponse):
    def __init__(self, msg: str, command: Command):
        super().__init__(
            f'ERROR WHEN EXECUTING {command.command.upper()} ',
            color=0xff0000,
            icon='❌',
            msg={
                "name": "Error Message",
                "value": command.error
            }
        )


class ApproveResponse(TextResponse):
    def __init__(self, msg: str, command: Command):
        super().__init__(
            f'ERROR WHEN EXECUTING {command.command.upper()} ',
            color=0xff0000,
            icon='✅',
            msg={
                "name": "Error Message",
                "value": command.error
            }
        )


class ImageResponse(discord.Embed):
    def __init__(self, title: str, url: str, color: int = 0xffffff, icon=""):
        super().__init__(title=f'{icon} {title}'.lstrip(" "), color=color)
        self.set_image(url=url)
