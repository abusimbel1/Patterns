from filters import FloatFilter, IntFilter, RangeFilter, AbsFilter, FilterPipe

arr_1 = [-1, -0.3, 0, 0.1, 1]
if __name__ == '__main__':

    positive_int_pipe = FilterPipe()
    positive_int_pipe.add_filter(AbsFilter(1), IntFilter())

    negative_float_pipe = FilterPipe()
    negative_float_pipe.add_filter(AbsFilter(-1), FloatFilter())

    print('Result for first case', positive_int_pipe.filter(arr_1))
    print('Result for second case', negative_float_pipe.filter(arr_1))