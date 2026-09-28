@pytest.mark.parametrize('input_class', [list, dict, OrderedDict])
def test_constructor_empty(self, input_class):
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        empty = Series()
        empty2 = Series(input_class())
    tm.assert_series_equal(empty, empty2, check_index_type=False)
    empty = Series(dtype='float64')
    empty2 = Series(input_class(), dtype='float64')
    tm.assert_series_equal(empty, empty2, check_index_type=False)
    empty = Series(dtype='category')
    empty2 = Series(input_class(), dtype='category')
    tm.assert_series_equal(empty, empty2, check_index_type=False)
    if input_class is not list:
        with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
            empty = Series(index=range(10))
            empty2 = Series(input_class(), index=range(10))
        tm.assert_series_equal(empty, empty2)
        empty = Series(np.nan, index=range(10))
        empty2 = Series(input_class(), index=range(10), dtype='float64')
        tm.assert_series_equal(empty, empty2)
        empty = Series('', dtype=str, index=range(3))
        empty2 = Series('', index=range(3))
        tm.assert_series_equal(empty, empty2)