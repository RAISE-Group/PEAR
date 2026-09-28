def test_is_dtype(self):
    assert CategoricalDtype.is_dtype(self.dtype)
    assert CategoricalDtype.is_dtype('category')
    assert CategoricalDtype.is_dtype(CategoricalDtype())
    assert not CategoricalDtype.is_dtype('foo')
    assert not CategoricalDtype.is_dtype(np.float64)