def test_equality(self):
    assert is_dtype_equal(self.dtype, 'category')
    assert is_dtype_equal(self.dtype, CategoricalDtype())
    assert not is_dtype_equal(self.dtype, 'foo')