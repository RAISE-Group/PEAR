def test_construction_from_string(self):
    result = CategoricalDtype.construct_from_string('category')
    assert is_dtype_equal(self.dtype, result)
    msg = "Cannot construct a 'CategoricalDtype' from 'foo'"
    with pytest.raises(TypeError, match=msg):
        CategoricalDtype.construct_from_string('foo')