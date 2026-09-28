def test_subtype_float(self, index):
    dtype = IntervalDtype('float64')
    msg = 'Cannot convert .* to .*; subtypes are incompatible'
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)