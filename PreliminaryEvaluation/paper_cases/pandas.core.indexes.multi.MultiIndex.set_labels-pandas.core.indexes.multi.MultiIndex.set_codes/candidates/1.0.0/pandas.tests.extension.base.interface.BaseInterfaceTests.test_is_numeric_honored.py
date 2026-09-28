def test_is_numeric_honored(self, data):
    result = pd.Series(data)
    assert result._data.blocks[0].is_numeric is data.dtype._is_numeric