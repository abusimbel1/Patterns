from masterSlave import Master
import asyncio


async def print_result():
    master = Master()

    res = await master.calculateResult([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    print(res)

if __name__ == "__main__":

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(print_result())
    event_loop.close()