from math import fabs


class Filter:
    def filter(self, value: float):
        return True

    def run(self, values):
        return [v for v in values if self.filter(v)]


class AbsFilter(Filter):
    sign = 1

    def __init__(self, sign=1):
        self.sign = sign

    def filter(self, value: float):
        return fabs(value) == value * self.sign


class IntFilter(Filter):
    def filter(self, value: float):
        return value % 1 == 0


class FloatFilter(Filter):
    def filter(self, value: float):
        return value % 1 != 0


class RangeFilter(Filter):
    min = None
    max = None

    def __init__(self, range_tuple):
        self.min, self.max = range_tuple

    def filter(self, value: float):
        return value > self.min and value < self.max


class FilterPipe:
    filters = []

    def __init__(self) -> None:
        self.filters = []

    def reset(self):
        self.filters = []

    def add_filter(self, *filters):
        self.filters += filters

    def filter(self, values):
        values_copy = values.copy()

        for filter_class in self.filters:
            values_copy = filter(filter_class.filter, values_copy)

        return list(values_copy)