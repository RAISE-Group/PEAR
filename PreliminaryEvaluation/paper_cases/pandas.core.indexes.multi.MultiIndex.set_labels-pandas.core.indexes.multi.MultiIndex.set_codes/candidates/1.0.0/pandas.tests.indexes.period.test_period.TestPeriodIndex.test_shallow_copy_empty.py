def test_shallow_copy_empty(self):
    idx = PeriodIndex([], freq='M')
    result = idx._shallow_copy()
    expected = idx
    tm.assert_index_equal(result, expected)