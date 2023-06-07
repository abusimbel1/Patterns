from master_slave import Master
import asyncio


async def main():
    master = Master()

    res = await master.calculate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    print(res)

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()