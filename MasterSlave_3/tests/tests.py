import unittest
from master_slave import is_prime, Master
import asyncio

loop = asyncio.get_event_loop()


def test_handler(v):
    return v


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(1), True)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(7), True)

    def test_floats(self):
        self.assertEqual(is_prime(0.5), False)

    def test_negatives(self):
        self.assertEqual(is_prime(-1), False)

    def test_zero(self):
        self.assertEqual(is_prime(0), False)


class TestCalculate(unittest.TestCase):

    def test_create_workers(self):
        master = Master()

        res = loop.run_until_complete(master.calculate([]))

        self.assertEqual(len(res), 5)

    def test_split_work(self):
        master = Master()

        res = loop.run_until_complete(master.calculate([1, 2, 3]))

        self.assertEqual(len(res), 5)
        self.assertEqual(len(res[0]), 1)
        self.assertEqual(len(res[1]), 1)
        self.assertEqual(len(res[2]), 1)

    def test_calc_results(self):
        master = Master()

        res = loop.run_until_complete(master.calculate([1, 2, 3]))

        self.assertEqual(res[0][0][1], is_prime(1))
        self.assertEqual(res[1][0][1], is_prime(2))
        self.assertEqual(res[2][0][1], is_prime(3))


if __name__ == "__main__":

    unittest.main()
    loop.close()