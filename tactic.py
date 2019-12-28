import logging
from account import Account, InvestRange
from config import mine_count, push_limit, invest_to


class Tactic:
    def __init__(self, account: Account, tactic: str, acc_name: str):
        self.account = account
        self.tactic = tactic
        self.acc_name = acc_name

    async def process(self):
        pass


class Simple(Tactic):
    """
    Обычная тактика.

    Майнит монеты. После достижения push_limit начинает инвестирует в количестве баланс аккаунта/8 на 10 минут (1.1х)
    """
    def __init__(self, account: Account, acc_name: str):
        super(Simple, self).__init__(account, "simple", acc_name)

    async def process(self):
        data = await self.account.mine(mine_count)
        if "balance" in data:
            logging.info(f"[{self.tactic}] {self.acc_name} balance: {data['balance']/100} (raw {data['balance']})")
            if data["balance"] >= push_limit:
                invest = await self.account.invest(
                    invest_to[0],
                    invest_to[1],
                    int((data["balance"]) / 100 / 8),
                    InvestRange.ten_min_x1dot1,
                )
                if invest["success"]:
                    logging.info(
                        f"[{self.tactic}] {self.acc_name} success invest: {data['balance'] / 100} "
                        f"(raw {data['balance']})")
                else:
                    logging.warning(
                        f"[{self.tactic}] {self.acc_name} unsuccess invest: {data['balance'] / 100} (raw "
                        f"{data['balance']})")
        else:
            logging.error(
                f"[{self.tactic}] {self.acc_name} {data}")
