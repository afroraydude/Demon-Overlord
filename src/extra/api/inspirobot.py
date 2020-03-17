# imports
import requests as req
import json
from . import api
# constructor
class InspirobotAPI(api.API):

    # stuff that happens on first call
    def __init__(self):
        super().__init__("", "inspirobot", "https://inspirobot.me")

    # get the list of stuff from inspirobot
    async def __get_flow(self):

        # let's try getting something
        try:
            # you know... i don't like that you treat me like an object... 
            url = f'{self.url}/api?generate=true'
            response = req.get(url)

            # YOU RAISE ME UUUUUUUP 
            response.raise_for_status()
        except Exception:

            # I've had enough of this... this is just WRONG
            return False
        else:

            # all is good, return the object
            return response.text

    # public function that gets data from inspiro and then gets the shortest quote
    async def get_quote(self):

        # get a flow and init quotes array
        img = await self.__get_flow()
        
        # FUCK, NO. WHY DOESN'T THIS WORK???? ~ Luzi
        if not img:
            return False

        # return the image
        return img