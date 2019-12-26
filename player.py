import asyncio
from account import Account
from tactic import Simple
from utils.task_manager import TaskManager
from config import sleep_after_mine

players = []

for i, sign_url in enumerate(open("accs.txt").read().split("\n")):
    acc = Account(sign_url)
    s = Simple(acc, str(i))
    players.append(s.process)


async def main():
    while True:
        for player_process in players:
            await player_process()
        await asyncio.sleep(sleep_after_mine)


loop = asyncio.get_event_loop()
task_manager = TaskManager(loop)
task_manager.add_task(main)
task_manager.run()
