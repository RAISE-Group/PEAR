def test_setitem_scalar_key_sequence_raise(self, data):
    arr = data[:5].copy()
    with pytest.raises(ValueError):
        arr[0] = arr[[0, 1]]