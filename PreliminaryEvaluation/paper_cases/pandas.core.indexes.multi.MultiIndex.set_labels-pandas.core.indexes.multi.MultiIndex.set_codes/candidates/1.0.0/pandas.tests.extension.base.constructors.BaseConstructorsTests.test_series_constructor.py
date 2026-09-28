def test_series_constructor(self, data):
    result = pd.Series(data)
    assert result.dtype == data.dtype
    assert len(result) == len(data)
    assert isinstance(result._data.blocks[0], ExtensionBlock)
    assert result._data.blocks[0].values is data
    result2 = pd.Series(result)
    assert result2.dtype == data.dtype
    assert isinstance(result2._data.blocks[0], ExtensionBlock)