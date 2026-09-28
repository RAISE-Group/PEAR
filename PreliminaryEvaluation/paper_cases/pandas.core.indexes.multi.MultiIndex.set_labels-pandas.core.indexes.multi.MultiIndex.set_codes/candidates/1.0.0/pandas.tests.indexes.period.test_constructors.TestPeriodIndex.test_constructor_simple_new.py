def test_constructor_simple_new(self):
    idx = period_range('2007-01', name='p', periods=2, freq='M')
    result = idx._simple_new(idx, name='p', freq=idx.freq)
    tm.assert_index_equal(result, idx)
    result = idx._simple_new(idx.astype('i8'), name='p', freq=idx.freq)
    tm.assert_index_equal(result, idx)