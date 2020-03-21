import discord



class TextResponse(discord.Embed):
    def __init__(self, title: str, color: int = 0xffffff, icon: str = "", msg: dict = None):
        super().__init__(title=f'{icon} {title}', color=color)

        if msg != None:
            self.add_field(name=msg["name"], value=msg["value"], inline=False)


class ApproveResponse(TextResponse):
    def __init__(self, msg: str, command):
        pass


class ErrorResponse(TextResponse):
    def __init__(self, command, tb):
        super().__init__(
            f'ERROR WHEN EXECUTING COMMAND: {command.action} ',
            color=0xff0000,
            icon='🚫'
        )
        self.add_field(name="Full Command:", value=command.full, inline=False)
        self.add_field(name="Traceback:", value=f'```\n{tb}\n```', inline=False)


class ImageResponse(discord.Embed):
    def __init__(self, title: str, url: str, color: int = 0xffffff, icon=""):
        super().__init__(title=f'{icon} {title}'.lstrip(" "), color=color)
        self.set_image(url=url)
