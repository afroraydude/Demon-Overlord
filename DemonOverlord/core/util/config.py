import discord
import os
import sys
import json

from DemonOverlord.core.util.api import TenorAPI, InspirobotAPI
from DemonOverlord.core.util.limit import RateLimiter


class BotConfig(object):

    def __init__(self, bot: discord.Client, confdir: str, argv: list):
        # set all vars None first, this also gives us a list of all currently available vars
        self.raw = None
        self.mode = None
        self.izzymojis = dict()
        self.token = None
        self.env = None

        # set all vars to their final value.

        # get the raw config.json
        with open(os.path.join(confdir, "config.json")) as f:
            self.raw = json.load(f)

        # generate izzymoji list
        for key in self.raw["izzymojis"].keys():
            self.izzymojis[key] = self.raw["izzymojis"][key]

        # create config from cli stuff
        for arg in argv:
            # set bot mode
            if arg in self.raw["cli_options"]["bot_modes"]:
                self.mode = self.raw["cli_options"]["bot_modes"][argv[1]]
            else:
                self.raw["cli_options"]["bot_modes"]["--prod"]
        print(self.mode)
        # set the token
        self.token = os.environ.get(self.mode["tokenvar"])
        self.env = self.raw["env_vars"]

    def check_config(self):
        if not self.raw:
            return False
        elif not self.mode:
            return False
        elif not self.izzymojis:
            return False
        elif not self.token:
            return False

        else:
            return True


class APIConfig(object):

    def __init__(self, config: BotConfig):
        # var init
        self.tenor = None
        self.inspirobot = InspirobotAPI()

        print(config.env)
        tenor_key = os.environ.get(config.env["api"]["tenor"][0])
        if tenor_key:
            self.tenor = TenorAPI(tenor_key)


class DatabaseConfig(object):
    def __init__(self):
        pass


class CommandConfig(object):

    def __init__(self, confdir: str):
        with open(os.path.join(confdir, "default_ratelimits.json")) as f:
            self.ratelimits = RateLimiter(json.load(f))

        with open(os.path.join(confdir, "special/interactions.json")) as f:
            self.interactions = json.load(f)

        with open(os.path.join(confdir, "special/relations.json")) as f:
            self.relations = json.load(f)


class HelpConfig(object):
    def __init__(self):
        pass


class RelationshipConfig(object):
    def __init__(self, db: DatabaseConfig):
        pass
