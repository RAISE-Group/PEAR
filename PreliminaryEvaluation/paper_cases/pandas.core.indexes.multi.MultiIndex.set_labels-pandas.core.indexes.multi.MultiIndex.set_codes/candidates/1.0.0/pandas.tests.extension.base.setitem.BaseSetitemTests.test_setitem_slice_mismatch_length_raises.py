def test_setitem_slice_mismatch_length_raises(self, data):
    arr = data[:5]
    with pytest.raises(ValueError):
        arr[:1] = arr[:2]