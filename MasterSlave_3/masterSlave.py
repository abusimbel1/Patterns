import asyncio


def is_prime(n):
    if (n < 1 or not float(n).is_integer()):
        return False

    for i in range(2, int(n)):
        if (n % i) == 0:
            return False
    return True


class Master:
    WORKERS_AMOUNT = 5

    def __init__(self) -> None:
        self.workers = [self.operation for _ in range(self.WORKERS_AMOUNT)]

    async def operation(self, values):
        await asyncio.sleep(1)
        return [(value, is_prime(value)) for value in values]

    async def calculate(self, values):
        sublists = [values[i::self.WORKERS_AMOUNT]
                    for i in range(self.WORKERS_AMOUNT)]

        return await asyncio.gather(*[self.operation(sublist) for sublist in sublists])