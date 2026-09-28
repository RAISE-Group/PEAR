@pytest.mark.parametrize('input_arg', [np.nan, float('nan')])
def test_constructor_nan(self, input_arg):
    empty = Series(dtype='float64', index=range(10))
    empty2 = Series(input_arg, index=range(10))
    tm.assert_series_equal(empty, empty2, check_index_type=False)