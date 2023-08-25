import asyncio
import random

loop = asyncio.get_event_loop()


async def execute_task():
    time_out = random.uniform(0.5, 5)
    print("Starting {:1.2f}..".format(time_out))
    await asyncio.sleep(time_out)
    print("Stoping {:1.2f}..".format(time_out))
    return time_out


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(execute_task()))
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")


results = loop.run_until_complete(main())
loop.close()
