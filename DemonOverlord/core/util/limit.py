import discord
from time import time


class RateLimiter:
    # create the rate limiter
    def __init__(self, limits_raw: dict):
        self.all = RateLimit(limits_raw["all"]["limit"], True)
        self.limits = {}
        self.lastExec = {}

        for key in limits_raw.keys():
            template = {
                "name": key,
                "ulist": list()
            }
            self.lastExec[key] = template
            if key != "all":
                self.limits[key] = RateLimit(
                    limits_raw[key]["limit"], True) # to be assumed true for now

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
        if not command.action in self.lastExec.keys():
            self.lastExec[command.action] = exec_template


        # is this command limited? overwrites global limis 
        if command.action in self.limits.keys():
            last_exec = list(filter(lambda x: x[1]["user"] == command.invoked_by.id, enumerate(
                self.lastExec[command.action]["ulist"])))

            if len(last_exec) > 0:

                if self.limits[command.action].test(int(time()), last_exec[0][1]):
                    self.lastExec[command.action]["ulist"][last_exec[0][0]]["timestamp"] = int(time())
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

        # do he have a global limit?
        if self.all.limit != 0:
            last_exec = list(filter(lambda x: x[1]["user"] == command.invoked_by.id, enumerate(
                self.lastExec["all"]["ulist"])))

            if len(last_exec) > 0:
                print(self.all.test(int(time()), last_exec[0][1]))
                if self.all.test(int(time()), last_exec[0][1]):
                    self.lastExec["all"]["ulist"][last_exec[0][0]]["timestamp"] = int(time())
                    return True
                else: 
                    return False

            else:
                # set the user profile, first execution so we can let it pass
                self.lastExec["all"]["ulist"].append(
                    {
                        "user": command.invoked_by.id,
                        "timestamp": int(time())
                    }
                )
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
