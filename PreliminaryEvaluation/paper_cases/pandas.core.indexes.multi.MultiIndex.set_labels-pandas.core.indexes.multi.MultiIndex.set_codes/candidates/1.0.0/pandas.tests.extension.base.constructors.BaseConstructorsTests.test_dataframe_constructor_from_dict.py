@pytest.mark.parametrize('from_series', [True, False])
def test_dataframe_constructor_from_dict(self, data, from_series):
    if from_series:
        data = pd.Series(data)
    result = pd.DataFrame({'A': data})
    assert result.dtypes['A'] == data.dtype
    assert result.shape == (len(data), 1)
    assert isinstance(result._data.blocks[0], ExtensionBlock)