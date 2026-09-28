@pytest.mark.parametrize('to_type', [tuple, list, np.array])
def test_get_complex_nested(self, to_type):
    values = Series([to_type([to_type([1, 2])])])
    result = values.str.get(0)
    expected = Series([to_type([1, 2])])
    tm.assert_series_equal(result, expected)
    result = values.str.get(1)
    expected = Series([np.nan])
    tm.assert_series_equal(result, expected)