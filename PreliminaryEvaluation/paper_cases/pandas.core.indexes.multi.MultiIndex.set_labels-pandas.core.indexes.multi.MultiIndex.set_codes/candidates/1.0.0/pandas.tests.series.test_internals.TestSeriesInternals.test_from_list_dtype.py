def test_from_list_dtype(self):
    result = pd.Series(['1H', '2H'], dtype='timedelta64[ns]')
    assert result._data.blocks[0].is_extension is False
    result = pd.Series(['2015'], dtype='datetime64[ns]')
    assert result._data.blocks[0].is_extension is False