import aiohttp


class InvestRange:
    ten_min_x1dot1 = 1
    thirty_min_x1dot4 = 2
    sixty_min_x2 = 3


class Account:
    url: str = "https://vkpredlojka.ru/server/"

    def __init__(self, sign_url: str):
        self.parsed_url = {
            x[0]: x[1]
            for x in [x.split("=") for x in sign_url.split("?")[1].split("&")]
        }
        self.parsed_url["vk_access_token_settings"] = self.parsed_url[
            "vk_access_token_settings"
        ].replace("%2C", ",")
        self.sign = self.parsed_url["sign"]
        del self.parsed_url["sign"]
        self.session = aiohttp.ClientSession()

    async def request(self, data):
        async with self.session.post(self.url, json=data) as resp:
            return await resp.json()

    def create_json(self, module: str, data: dict) -> dict:
        """Создает жсон для запросов"""

        return dict(module=module, data=data, get=self.parsed_url, sign=self.sign)

    async def mine(self, count: int):
        """Майнит count монет за один запрос"""
        payload = self.create_json("ping", dict(mined=count))
        return await self.request(payload)

    async def invest(
        self, to_type: str, to_id: int, amount: int, invest_range: InvestRange
    ):
        payload = self.create_json(
            "invest", dict(type=to_type, id=to_id, amount=amount, range=invest_range)
        )
        return await self.request(payload)
