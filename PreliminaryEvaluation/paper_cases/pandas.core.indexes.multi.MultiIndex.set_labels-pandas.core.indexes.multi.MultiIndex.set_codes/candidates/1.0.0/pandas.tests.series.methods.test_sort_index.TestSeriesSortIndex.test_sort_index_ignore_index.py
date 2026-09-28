@pytest.mark.parametrize('inplace', [True, False])
@pytest.mark.parametrize('original_list, sorted_list, ascending, ignore_index, output_index', [([2, 3, 6, 1], [2, 3, 6, 1], True, True, [0, 1, 2, 3]), ([2, 3, 6, 1], [2, 3, 6, 1], True, False, [0, 1, 2, 3]), ([2, 3, 6, 1], [1, 6, 3, 2], False, True, [0, 1, 2, 3]), ([2, 3, 6, 1], [1, 6, 3, 2], False, False, [3, 2, 1, 0])])
def test_sort_index_ignore_index(self, inplace, original_list, sorted_list, ascending, ignore_index, output_index):
    ser = Series(original_list)
    expected = Series(sorted_list, index=output_index)
    kwargs = {'ascending': ascending, 'ignore_index': ignore_index, 'inplace': inplace}
    if inplace:
        result_ser = ser.copy()
        result_ser.sort_index(**kwargs)
    else:
        result_ser = ser.sort_index(**kwargs)
    tm.assert_series_equal(result_ser, expected)
    tm.assert_series_equal(ser, Series(original_list))