import time
from functools import partial
import asyncio
from concurrent.futures import ThreadPoolExecutor

def blocking_work(seconds: int):
    print('blocking work: starting')
    time.sleep(seconds)
    print('blocking work: done')

async def work(seconds: int):
    print('work: starting')
    await asyncio.sleep(seconds)
    print('work: done')

async def main():
    task = asyncio.create_task(work(1))
    print(task)
    await asyncio.sleep(3)
    print(task)

async def main2():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, partial(blocking_work, 1))
    await asyncio.sleep(3)

async def main3():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=1) as executor:
        loop.run_in_executor(executor, partial(blocking_work, 1))
        await asyncio.sleep(3)

    
if __name__ == '__main__':
    asyncio.run(main3(), debug=True)
