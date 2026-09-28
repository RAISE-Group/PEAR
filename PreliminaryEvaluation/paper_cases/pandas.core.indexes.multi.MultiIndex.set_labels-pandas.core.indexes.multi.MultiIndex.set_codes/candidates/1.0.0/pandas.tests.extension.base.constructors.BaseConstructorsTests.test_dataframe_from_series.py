def test_dataframe_from_series(self, data):
    result = pd.DataFrame(pd.Series(data))
    assert result.dtypes[0] == data.dtype
    assert result.shape == (len(data), 1)
    assert isinstance(result._data.blocks[0], ExtensionBlock)