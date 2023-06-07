from filters import FloatFilter, IntFilter, RangeFilter, AbsFilter, FilterPipe

arr_1 = [-1, -0.5, 0, 0.5, 1]
if __name__ == '__main__':

    positive_int_pipe = FilterPipe()
    positive_int_pipe.add_filter(AbsFilter(1), IntFilter())

    negative_float_pipe = FilterPipe()
    negative_float_pipe.add_filter(AbsFilter(-1), FloatFilter())

    print('res 1', positive_int_pipe.filter(arr_1))
    print('res 2', negative_float_pipe.filter(arr_1))