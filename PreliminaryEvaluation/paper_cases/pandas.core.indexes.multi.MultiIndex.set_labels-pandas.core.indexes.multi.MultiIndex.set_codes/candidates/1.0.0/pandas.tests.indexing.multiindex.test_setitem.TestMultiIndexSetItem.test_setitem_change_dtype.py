def test_setitem_change_dtype(self, multiindex_dataframe_random_data):
    frame = multiindex_dataframe_random_data
    dft = frame.T
    s = dft['foo', 'two']
    dft['foo', 'two'] = s > s.median()
    tm.assert_series_equal(dft['foo', 'two'], s > s.median())
    reindexed = dft.reindex(columns=[('foo', 'two')])
    tm.assert_series_equal(reindexed['foo', 'two'], s > s.median())