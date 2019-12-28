import asyncio
import logging
from account import Account
from tactic import Simple
from utils.task_manager import TaskManager
from config import sleep_after_mine, accs_file_name, logformat, logfile


def create_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(logformat)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.FileHandler(logfile, 'a')
    logger.addHandler(fh)
    fh.setFormatter(formatter)


players = []
create_logger()
for i, sign_url in enumerate(open(accs_file_name).read().split("\n")):
    acc = Account(sign_url)
    s = Simple(acc, str(i))
    logging.info(f"Loaded account {i}: {acc}")
    players.append(s.process)


async def main():
    logging.info("Launching bot...")
    while True:
        for player_process in players:
            await player_process()
        await asyncio.sleep(sleep_after_mine)


loop = asyncio.get_event_loop()
task_manager = TaskManager(loop)
task_manager.add_task(main)
task_manager.run()
