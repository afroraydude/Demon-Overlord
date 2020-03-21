# imports
import requests as req
import json
from random import randint
from . import api

class TenorAPI(api.API):
    def __init__(self, apikey:str):
        super().__init__(apikey, "tenor", "https://api.tenor.com/v1")
    
    async def get_interact(self: object, name: str) -> str:
        res = await self.__request_list(name, 20)
        res_list = list(res["results"])

        index = randint(0, len(res_list)-1)
        result = res_list[index]["media"][0]["gif"]["url"]
        return result

    async def __request_list(self: object, query: str, limit: int) -> object:
        try:
            url = f'{self.url}/search?q={query.replace(" ", "+")}&key={self.apikey}&limit={limit}'
            response = req.get(url)
            response.raise_for_status()
        except Exception:
            return False
        else:
            return json.loads(response.text)
