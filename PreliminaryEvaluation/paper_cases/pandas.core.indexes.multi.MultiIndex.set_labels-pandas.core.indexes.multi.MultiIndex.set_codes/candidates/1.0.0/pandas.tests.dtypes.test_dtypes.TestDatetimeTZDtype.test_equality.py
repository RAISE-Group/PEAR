def test_equality(self):
    assert is_dtype_equal(self.dtype, 'datetime64[ns, US/Eastern]')
    assert is_dtype_equal(self.dtype, DatetimeTZDtype('ns', 'US/Eastern'))
    assert not is_dtype_equal(self.dtype, 'foo')
    assert not is_dtype_equal(self.dtype, DatetimeTZDtype('ns', 'CET'))
    assert not is_dtype_equal(DatetimeTZDtype('ns', 'US/Eastern'), DatetimeTZDtype('ns', 'US/Pacific'))
    assert is_dtype_equal(np.dtype('M8[ns]'), 'datetime64[ns]')