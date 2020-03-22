import discord
from time import time


class RateLimiter(object):
    # create the rate limiter
    def __init__(self, cmd_list: dict):
        self.limits = {}
        self.lastExec = {}
        for i in cmd_list:
            exec_template = {
                "name": i["command"],
                "ulist": []
            }
            self.limits[i["command"]] = RateLimit(
                i["ratelimit"]["limit"], i["ratelimit"]["user_dependent"])

    # use the ratelimiter

    def exec(self, command) -> tuple:
        user_template = {
            "user": command.invoked_by.id,
            "timestamp": 0
        }
        # is this command limited? overwrites global limis
        if self.limits[command.command].limit > 0:
            last_exec = list(filter(lambda x: x[1]["user"] == command.invoked_by.id, enumerate(
                self.lastExec[command.action]["ulist"])))

            if len(last_exec) > 0:

                if self.limits[command.action].test(int(time()), last_exec[0][1]):
                    self.lastExec[command.action]["ulist"][last_exec[0]
                                                           [0]]["timestamp"] = int(time())
                    return True
                else:
                    return False

            else:
                # set the user profile, first execution so we can let it pass
                self.lastExec[command.action]["ulist"].append(
                    {
                        "user": command.invoked_by.id,
                        "timestamp": int(time())
                    }
                )
                return True
        else:
            return True


# rate limit object
class RateLimit(object):
    def __init__(self, limit: int, user_dependent: bool):
        self.limit = limit
        self.user_dependent = user_dependent

    def test(self, time: int, lastExec: dict) -> bool:
        if time - lastExec["timestamp"] < self.limit:
            return False
        return True

    def __str__(self):
        return f'{self.limit} - {self.user_dependent}'