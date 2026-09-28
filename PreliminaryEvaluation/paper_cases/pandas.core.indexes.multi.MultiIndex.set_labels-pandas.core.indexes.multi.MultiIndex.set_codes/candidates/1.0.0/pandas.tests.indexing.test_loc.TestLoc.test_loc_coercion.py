def test_loc_coercion(self):
    df = DataFrame({'date': [Timestamp('20130101').tz_localize('UTC'), pd.NaT]})
    expected = df.dtypes
    result = df.iloc[[0]]
    tm.assert_series_equal(result.dtypes, expected)
    result = df.iloc[[1]]
    tm.assert_series_equal(result.dtypes, expected)
    import datetime
    df = DataFrame({'date': [datetime.datetime(2012, 1, 1), datetime.datetime(1012, 1, 2)]})
    expected = df.dtypes
    result = df.iloc[[0]]
    tm.assert_series_equal(result.dtypes, expected)
    result = df.iloc[[1]]
    tm.assert_series_equal(result.dtypes, expected)
    df = DataFrame({'text': ['some words'] + [None] * 9})
    expected = df.dtypes
    result = df.iloc[0:2]
    tm.assert_series_equal(result.dtypes, expected)
    result = df.iloc[3:]
    tm.assert_series_equal(result.dtypes, expected)