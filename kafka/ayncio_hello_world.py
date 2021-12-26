import asyncio
from time import sleep

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
sleep(2)
print('Hello..')
sleep(2)
print('..there!')
sleep(2)