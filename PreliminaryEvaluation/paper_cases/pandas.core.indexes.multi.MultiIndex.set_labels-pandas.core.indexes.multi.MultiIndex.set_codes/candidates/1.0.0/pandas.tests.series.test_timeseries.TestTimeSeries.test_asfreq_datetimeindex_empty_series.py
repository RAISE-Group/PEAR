def test_asfreq_datetimeindex_empty_series(self):
    index = pd.DatetimeIndex(['2016-09-29 11:00'])
    expected = Series(index=index, dtype=object).asfreq('H')
    result = Series([3], index=index.copy()).asfreq('H')
    tm.assert_index_equal(expected.index, result.index)