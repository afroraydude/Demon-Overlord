# imports
import requests as req
import json
from random import randint


class API:
    def __init__(self, apikey:str, name:str, url:str):
        self.apikey = apikey
        self.name = name
        self.url = url



class TenorAPI(API):
    def __init__(self, apikey:str):
        super().__init__(apikey, "tenor", "https://api.tenor.com/v1")
    
    async def get_interact(self, name: str) -> str:
        res = await self.__request_list(name, 20)
        res_list = list(res["results"])

        index = randint(0, len(res_list)-1)
        result = res_list[index]["media"][0]["gif"]["url"]
        return result

    async def __request_list(self: object, query: str, limit: int) -> dict:
        try:
            url = f'{self.url}/search?q={query.replace(" ", "+")}&key={self.apikey}&limit={limit}'
            response = req.get(url)
            response.raise_for_status()
        except Exception:
            return False
        else:
            return json.loads(response.text)


class InspirobotAPI(API):

    # stuff that happens on first call
    def __init__(self):
        super().__init__("", "inspirobot", "https://inspirobot.me")

    # get the list of stuff from inspirobot
    async def __get_flow(self) -> str:

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
    async def get_quote(self) -> str:

        # get a flow and init quotes array
        img = await self.__get_flow()
        
        # FUCK, NO. WHY DOESN'T THIS WORK???? ~ Luzi
        if not img:
            return False

        # return the image
        return img