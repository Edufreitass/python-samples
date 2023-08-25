import asyncio
import random

# async def alpha(x):
#     await asyncio.sleep(0.2)
#     return x + 1
#
#
# async def bravo(x):
#     await asyncio.sleep(0.2)
#     return random.randint(0, 1000) + x
#
#
# async def charlie(x):
#     if x % 2 == 0:
#         return x
#     raise ValueError(x, 'is odd')
#
#
# async def run():
#     try:
#         number = await charlie(await bravo(await alpha(42)))
#     except ValueError as exc:
#         print('error:', exc.args[0])
#     else:
#         print('success:', number)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run())
#     loop.close()

# import asyncio
# from aiostream import stream, pipe
#
#
# async def main():
#     # This stream computes 11² + 13² in 1.5 second
#     xs = (
#             stream.count(interval=0.1)  # Count from zero every 0.1 s
#             | pipe.skip(10)  # Skip the first 10 numbers
#             | pipe.take(5)  # Take the following 5
#             | pipe.filter(lambda x: x % 2)  # Keep odd numbers
#             | pipe.map(lambda x: x ** 2)  # Square the results
#             | pipe.accumulate()  # Add the numbers together
#     )
#     print('11² + 13² = ', await xs)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()
