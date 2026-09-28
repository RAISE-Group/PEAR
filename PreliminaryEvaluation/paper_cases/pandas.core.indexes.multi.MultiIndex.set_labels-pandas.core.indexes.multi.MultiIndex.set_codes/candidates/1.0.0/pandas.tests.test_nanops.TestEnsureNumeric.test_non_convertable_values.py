def test_non_convertable_values(self):
    msg = 'Could not convert foo to numeric'
    with pytest.raises(TypeError, match=msg):
        nanops._ensure_numeric('foo')
    msg = 'argument must be a string or a number'
    with pytest.raises(TypeError, match=msg):
        nanops._ensure_numeric({})
    with pytest.raises(TypeError, match=msg):
        nanops._ensure_numeric([])