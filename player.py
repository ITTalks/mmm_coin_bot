import asyncio
from account import Account
from tactic import Simple
from utils.task_manager import TaskManager

players = []

for i, sign_url in enumerate(open("accs.txt")):
    acc = Account(sign_url[:-1])
    s = Simple(acc, i)
    players.append(s.process)


async def main():
    while True:
        for p in players:
            await p()

loop = asyncio.get_event_loop()
task_manager = TaskManager(loop)
task_manager.add_task(main)
task_manager.run()
