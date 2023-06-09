import asyncio

class Master:
    NUM_OF_PATCHES = 3

    def __init__(self) -> None:
        self.workers = [self.operation for _ in range(self.NUM_OF_PATCHES)]

    async def operation(self, values):
        await asyncio.sleep(1)
        return [(value, number_is_prime(value)) for value in values]

    async def calculateResult(self, values):
        sublists = [values[i::self.NUM_OF_PATCHES]
                    for i in range(self.NUM_OF_PATCHES)]

        return await asyncio.gather(*[self.operation(sublist) for sublist in sublists])

def number_is_prime(n):
    if (n < 1 or not float(n).is_integer()):
        return False

    for i in range(2, int(n)):
        if (n % i) == 0:
            return False
    return True