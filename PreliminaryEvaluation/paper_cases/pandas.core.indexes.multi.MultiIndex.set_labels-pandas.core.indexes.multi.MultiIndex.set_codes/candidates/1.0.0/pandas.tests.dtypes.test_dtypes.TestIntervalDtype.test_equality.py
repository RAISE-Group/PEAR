def test_equality(self):
    assert is_dtype_equal(self.dtype, 'interval[int64]')
    assert is_dtype_equal(self.dtype, IntervalDtype('int64'))
    assert is_dtype_equal(IntervalDtype('int64'), IntervalDtype('int64'))
    assert not is_dtype_equal(self.dtype, 'int64')
    assert not is_dtype_equal(IntervalDtype('int64'), IntervalDtype('float64'))
    dtype1 = IntervalDtype('float64')
    dtype2 = IntervalDtype('datetime64[ns, US/Eastern]')
    assert dtype1 != dtype2
    assert dtype2 != dtype1