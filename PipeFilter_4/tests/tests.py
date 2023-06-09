import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from filters import AbsFilter, FloatFilter, IntFilter

class TestFloatFilter(unittest.TestCase):
    def setUp(self):
        self.filter = FloatFilter()

    def test_filters_negative(self):
        self.assertEqual(self.filter.filter(-1), False)
        self.assertEqual(self.filter.filter(-0.5), True)

    def test_filters_negative(self):
        self.assertEqual(self.filter.filter(1), False)
        self.assertEqual(self.filter.filter(0.5), True)

    def test_filters_zero(self):
        self.assertEqual(self.filter.filter(0), False)


class TestIntFilter(unittest.TestCase):
    def setUp(self):
        self.filter = IntFilter()

    def test_filters_negative(self):
        self.assertEqual(self.filter.filter(-1), True)
        self.assertEqual(self.filter.filter(-0.5), False)

    def test_filters_negative(self):
        self.assertEqual(self.filter.filter(1), True)
        self.assertEqual(self.filter.filter(0.5), False)

    def test_filters_zero(self):
        self.assertEqual(self.filter.filter(0), True)


class TestAbsFilter(unittest.TestCase):
    def setUp(self):
        self.filter = AbsFilter()

    def test_filters_negative(self):
        filter = AbsFilter(-1)

        self.assertEqual(filter.filter(-1), True)
        self.assertEqual(filter.filter(-0.5), True)
        self.assertEqual(filter.filter(0), True)
        self.assertEqual(filter.filter(1), False)

    def test_filters_positive(self):
        filter = AbsFilter(1)

        self.assertEqual(filter.filter(-1), False)
        self.assertEqual(filter.filter(-0.5), False)
        self.assertEqual(filter.filter(0), True)
        self.assertEqual(filter.filter(1), True)


if __name__ == "__main__":
    unittest.main()