def test_equality(self):
    assert is_dtype_equal(self.dtype, 'period[D]')
    assert is_dtype_equal(self.dtype, PeriodDtype('D'))
    assert is_dtype_equal(self.dtype, PeriodDtype('D'))
    assert is_dtype_equal(PeriodDtype('D'), PeriodDtype('D'))
    assert not is_dtype_equal(self.dtype, 'D')
    assert not is_dtype_equal(PeriodDtype('D'), PeriodDtype('2D'))