def test_fillna_length_mismatch(self, data_missing):
    msg = "Length of 'value' does not match."
    with pytest.raises(ValueError, match=msg):
        data_missing.fillna(data_missing.take([1]))