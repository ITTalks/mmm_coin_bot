import aiohttp


class Account:
    url: str = "https://vkpredlojka.ru/server/"

    def __init__(self, sign: str, user_id: int):
        self.user_id = user_id
        self.sign = sign
        self.session = aiohttp.ClientSession()

    async def request(self, data):
        async with self.session.post(self.url, json=data) as resp:
            return await resp.json()

    def create_json(self, module: str, data: dict) -> dict:
        """Создает жсон для запросов"""

        return dict(module=module, data=data,
                    get={
                        "vk_access_token_settings": "notify",
                        "vk_app_id": "7252470",
                        "vk_are_notifications_enabled": "0",
                        "vk_is_app_user": "1",
                        "vk_is_favorite": "0",
                        "vk_language": "ru",
                        "vk_platform": "desktop_web",
                        "vk_ref": "other",
                        "vk_user_id": self.user_id},
                    sign=self.sign)

    async def mine(self, count):
        """Майнит count монет за один запрос"""
        payload = self.create_json("ping", dict(minied=count))
        return await self.request(payload)
