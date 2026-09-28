@pytest.mark.parametrize('inplace', [True, False])
@pytest.mark.parametrize('original_list, sorted_list, ignore_index, output_index', [([2, 3, 6, 1], [6, 3, 2, 1], True, [0, 1, 2, 3]), ([2, 3, 6, 1], [6, 3, 2, 1], False, [2, 1, 0, 3])])
def test_sort_values_ignore_index(self, inplace, original_list, sorted_list, ignore_index, output_index):
    ser = Series(original_list)
    expected = Series(sorted_list, index=output_index)
    kwargs = {'ignore_index': ignore_index, 'inplace': inplace}
    if inplace:
        result_ser = ser.copy()
        result_ser.sort_values(ascending=False, **kwargs)
    else:
        result_ser = ser.sort_values(ascending=False, **kwargs)
    tm.assert_series_equal(result_ser, expected)
    tm.assert_series_equal(ser, Series(original_list))