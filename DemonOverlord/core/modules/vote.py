import discord

from DemonOverlord.core.util.responses import TextResponse, BadCommandResponse


async def handler(command) -> discord.Embed:
    if command.action == "create":
        vote_args = " ".join(command.params).split(";")
        vote = {
            "name": vote_args[0],
            "options": vote_args[-1] # options always come last
        }
        if len(vote_args) == 3:
            vote["description"] = vote_args[1]

        



class VoteMessage(TextResponse):
    def __init__(self, command, vote: dict):
        super().__init__(f'Vote', color=0x2250af,
                         icon=command.bot.config.izzymojis["izzyyay"])
        self.name = vote["name"]
        self.description = vote["description"] if "description" in vote.keys(
        ) else None
        self.options = vote["options"]


class VoteResult(TextResponse):
    pass
