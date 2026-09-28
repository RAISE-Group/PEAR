def test_non_scalar_raises(self, data_missing):
    msg = "Got a 'list' instead."
    with pytest.raises(TypeError, match=msg):
        data_missing.fillna([1, 1])