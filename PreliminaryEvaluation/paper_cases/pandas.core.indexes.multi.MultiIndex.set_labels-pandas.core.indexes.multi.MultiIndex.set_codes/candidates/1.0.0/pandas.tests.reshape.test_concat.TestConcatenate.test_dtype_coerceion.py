def test_dtype_coerceion(self):
    df = DataFrame({'date': [pd.Timestamp('20130101').tz_localize('UTC'), pd.NaT]})
    result = concat([df.iloc[[0]], df.iloc[[1]]])
    tm.assert_series_equal(result.dtypes, df.dtypes)
    import datetime
    df = DataFrame({'date': [datetime.datetime(2012, 1, 1), datetime.datetime(1012, 1, 2)]})
    result = concat([df.iloc[[0]], df.iloc[[1]]])
    tm.assert_series_equal(result.dtypes, df.dtypes)
    df = DataFrame({'text': ['some words'] + [None] * 9})
    result = concat([df.iloc[[0]], df.iloc[[1]]])
    tm.assert_series_equal(result.dtypes, df.dtypes)