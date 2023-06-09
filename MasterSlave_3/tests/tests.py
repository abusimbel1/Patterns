import sys
import os
import unittest
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from masterSlave import number_is_prime, Master

event_loop = asyncio.get_event_loop()

class TestCalculate(unittest.TestCase):

    def test_calc_results(self):
        master = Master()

        res = event_loop.run_until_complete(master.calculateResult([5, 7, 9]))

        self.assertEqual(res[0][0][1], number_is_prime(5))
        self.assertEqual(res[1][0][1], number_is_prime(7))
        self.assertEqual(res[2][0][1], number_is_prime(9))

    def test_create_workers(self):
        master = Master()

        res = event_loop.run_until_complete(master.calculateResult([]))

        self.assertEqual(len(res), 3)

    def test_split_work(self):
        master = Master()

        res = event_loop.run_until_complete(master.calculateResult([5, 7, 9]))

        self.assertEqual(len(res), 3)
        self.assertEqual(len(res[0]), 1)
        self.assertEqual(len(res[1]), 1)
        self.assertEqual(len(res[2]), 1)

class TestNumberIsPrime(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(number_is_prime(0), False)

    def test_is_prime(self):
        self.assertEqual(number_is_prime(1), True)
        self.assertEqual(number_is_prime(5), True)
        self.assertEqual(number_is_prime(6), False)
        self.assertEqual(number_is_prime(7), True)
        self.assertEqual(number_is_prime(9), False)
        self.assertEqual(number_is_prime(11), True)

    def test_floats_numbers(self):
        self.assertEqual(number_is_prime(0.5), False)

    def test_negatives(self):
        self.assertEqual(number_is_prime(-1), False)


if __name__ == "__main__":

    unittest.main()
    event_loop.close()