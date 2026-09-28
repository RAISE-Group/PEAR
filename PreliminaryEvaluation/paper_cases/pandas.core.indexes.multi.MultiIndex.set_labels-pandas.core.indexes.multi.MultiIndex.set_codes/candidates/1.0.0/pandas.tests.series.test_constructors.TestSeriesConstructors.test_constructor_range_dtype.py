@pytest.mark.parametrize('dtype', [None, 'uint8', 'category'])
def test_constructor_range_dtype(self, dtype):
    expected = Series([0, 1, 2, 3, 4], dtype=dtype or 'int64')
    result = Series(range(5), dtype=dtype)
    tm.assert_series_equal(result, expected)