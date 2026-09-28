def test_from_array(self):
    result = pd.Series(pd.array(['1H', '2H'], dtype='timedelta64[ns]'))
    assert result._data.blocks[0].is_extension is False
    result = pd.Series(pd.array(['2015'], dtype='datetime64[ns]'))
    assert result._data.blocks[0].is_extension is False