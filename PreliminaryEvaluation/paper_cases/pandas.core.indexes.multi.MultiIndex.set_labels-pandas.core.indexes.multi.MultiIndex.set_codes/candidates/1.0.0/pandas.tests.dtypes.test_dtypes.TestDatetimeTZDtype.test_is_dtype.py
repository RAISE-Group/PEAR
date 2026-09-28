def test_is_dtype(self):
    assert not DatetimeTZDtype.is_dtype(None)
    assert DatetimeTZDtype.is_dtype(self.dtype)
    assert DatetimeTZDtype.is_dtype('datetime64[ns, US/Eastern]')
    assert not DatetimeTZDtype.is_dtype('foo')
    assert DatetimeTZDtype.is_dtype(DatetimeTZDtype('ns', 'US/Pacific'))
    assert not DatetimeTZDtype.is_dtype(np.float64)