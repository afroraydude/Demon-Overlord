import discord
import os, sys
import json



class BotConfig(object):
    __slots__ = (
        "raw", "token", "izzymojis", "prefix"
    )
    def __init__(self, confdir:str):
        with open(os.path.join(confdir, "config.json")) as f:
            self.raw = json.load(f)

        # generate izzymoji list
        for key in self.raw["izzymojis"].keys():
            self.izzymojis[key] = self.raw["izzymojis"]
        
        self.prefix = self.raw["default_prefix"]

class DatabaseConfig(object):
    pass


class CommandConfig(object):
    __slots__ = (
        "ratelimits", "interactions", "relations"
    )
    def __init__(self, confdir:str):
        with open(os.path.join(confdir, "default_ratelimits.json")) as f:
            self.ratelimits = json.load(f)
            
        with open(os.path.join(confdir, "interactions.json")) as f:
            self.interactions = json.load(f)

        with open(os.path.join(confdir, "interactions.json")) as f:
            self.relations = json.load(f)


class HelpConfig(obj):
    def __init__(self):
        pass


