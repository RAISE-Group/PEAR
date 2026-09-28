def test_constructor_simple_new_empty(self):
    idx = PeriodIndex([], freq='M', name='p')
    result = idx._simple_new(idx, name='p', freq='M')
    tm.assert_index_equal(result, idx)