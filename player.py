import asyncio
import logging
from utils.task_manager import TaskManager
from account import Account


async def main():
    a = Account("") # your apps.get mobile_iframe
    while True:
        data = await a.mine(200)
        # i should use logging here!
        print(data)
        await asyncio.sleep(20)


loop = asyncio.get_event_loop()
task_manager = TaskManager(loop)
task_manager.add_task(main)
task_manager.run()
