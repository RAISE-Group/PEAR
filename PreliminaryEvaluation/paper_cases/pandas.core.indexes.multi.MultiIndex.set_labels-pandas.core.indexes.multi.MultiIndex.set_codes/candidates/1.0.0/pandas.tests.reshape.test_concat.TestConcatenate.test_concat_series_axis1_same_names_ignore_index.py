def test_concat_series_axis1_same_names_ignore_index(self):
    dates = date_range('01-Jan-2013', '01-Jan-2014', freq='MS')[0:-1]
    s1 = Series(randn(len(dates)), index=dates, name='value')
    s2 = Series(randn(len(dates)), index=dates, name='value')
    result = concat([s1, s2], axis=1, ignore_index=True)
    expected = Index([0, 1])
    tm.assert_index_equal(result.columns, expected)