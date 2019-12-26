import aiohttp


class Account:

    url: str = "https://vkpredlojka.ru/server/"

    def __init__(self, sign: str):
        self.sign = sign
        self.session = aiohttp.ClientSession()

    async def request(self, data):
        async with self.session.post(self.url, data=data) as resp:
            return await resp.json()

    def create_json(self, module: str, data: dict) -> dict:
        """Создает жсон для запросов"""
        return dict(module=module, data=data, sign=self.sign)

    async def mine(self, count):
        """Майнит count монет за один запрос"""
        payload = self.create_json("ping", dict(minied=count))
        return await self.request(payload)
