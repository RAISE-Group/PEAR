def test_equality_invalid(self):
    assert not self.dtype == 'foo'
    assert not is_dtype_equal(self.dtype, np.int64)