import discord
from time import time


class RateLimiter:
    # create the rate limiter
    def __init__(self, limits_raw: dict):
        self.all = limits_raw["all"]
        self.limits = {}
        self.lastExec = {}

        for key in limits_raw.keys():
            if key != "all":
                self.limits[key] = RateLimit(
                    limits_raw[key]["limit"], limits_raw[key]["user_dependent"])

    # use the ratelimiter
    def exec(self, command) -> bool:
        exec_template = {
            "name": command.action,
            "ulist": [
                {
                    "user": command.invoked_by.id,
                    "timestamp": 0
                }
            ]
        }

        # is it registered at all??
        if not command.action in self.lastExec and not command.action in self.limits:
            self.lastExec[command.action] = exec_template
            self.limits[command.action] = RateLimit(0, True)

        # welp we know the command but it hasn't been used yet
        if not command.action in self.lastExec and command.action in self.limits:
            self.lastExec[command.action] = exec_template

        # do he have a global limit?
        if self.all != 0:
            if int(time()) - self.lastExec["all"] <= self.all:
                return False
            else:
                self.lastExec["all"] = time()
                return True

        # do we have a comand limit?
        elif command.action in self.limits.keys():
            if self.limits[command.action].limt == 0:
                return True
            else:
                if self.limits[command.action].user_dependent:
                    last_exec = list(filter(lambda x: x[1]["user"] == command.invoked_by.id, enumerate(
                        self.lastExec[command.action]["ulist"])))

                    # user has used this command before
                    if len(last_exec) > 0:
                        allow = self.limits[command.action].test(
                            int(time()), last_exec[0][1])
                        self.lastExec[command.action]["ulist"][last_exec[0][0]]["timestamp"] = int(
                            time())
                        return allow

                    # user never used this command
                    else:
                        # set the user profile, first execution so we can let it pass
                        self.lastExec[command.action].append({
                            {
                                "user": command.invoked_by.id,
                                "timestamp": int(time())
                            }
                        })
                        return True
        else: 
            return False
                    


# rate limit object
class RateLimit:
    def __init__(self, limit: int, user_dependent: bool):
        self.limit = limit
        self.user_dependent = user_dependent

    def test(self, time: int, lastExec: dict) -> bool:
        if time - lastExec["timestamp"] < self.limit:
            return False
        return True
