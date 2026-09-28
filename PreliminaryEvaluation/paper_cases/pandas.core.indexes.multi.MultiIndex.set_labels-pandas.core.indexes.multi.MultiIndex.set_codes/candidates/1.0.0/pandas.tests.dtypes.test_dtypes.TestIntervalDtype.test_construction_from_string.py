def test_construction_from_string(self):
    result = IntervalDtype('interval[int64]')
    assert is_dtype_equal(self.dtype, result)
    result = IntervalDtype.construct_from_string('interval[int64]')
    assert is_dtype_equal(self.dtype, result)