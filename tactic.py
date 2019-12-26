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
    def __init__(self, account: Account, acc_name: str):
        super(Simple, self).__init__(account, "simple", acc_name)

    async def process(self):
        data = await self.account.mine(mine_count)
        if "balance" in data:
            print(f"{self.acc_name}: [BALANCE] = {data['balance']}")
            if data["balance"] >= push_limit:
                invest = await self.account.invest(
                    invest_to[0],
                    invest_to[1],
                    int((data["balance"]) / 100 / 2),
                    InvestRange.sixty_min_x2,
                )
                if invest["success"]:
                    print(f"{self.acc_name}: [SUCCESS INVEST] = {data['balance']}")
                else:
                    print(f"{self.acc_name}: [UNSUCCESS INVEST] = {data}")
        else:
            print(f"{self.acc_name}: [ERROR] No balance. Current data: {data}")
