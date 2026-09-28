def test_concat_NaT_series(self):
    x = Series(date_range('20151124 08:00', '20151124 09:00', freq='1h', tz='US/Eastern'))
    y = Series(pd.NaT, index=[0, 1], dtype='datetime64[ns, US/Eastern]')
    expected = Series([x[0], x[1], pd.NaT, pd.NaT])
    result = concat([x, y], ignore_index=True)
    tm.assert_series_equal(result, expected)
    expected = Series(pd.NaT, index=range(4), dtype='datetime64[ns, US/Eastern]')
    result = pd.concat([y, y], ignore_index=True)
    tm.assert_series_equal(result, expected)
    x = pd.Series(pd.date_range('20151124 08:00', '20151124 09:00', freq='1h'))
    y = pd.Series(pd.date_range('20151124 10:00', '20151124 11:00', freq='1h'))
    y[:] = pd.NaT
    expected = pd.Series([x[0], x[1], pd.NaT, pd.NaT])
    result = pd.concat([x, y], ignore_index=True)
    tm.assert_series_equal(result, expected)
    x[:] = pd.NaT
    expected = pd.Series(pd.NaT, index=range(4), dtype='datetime64[ns]')
    result = pd.concat([x, y], ignore_index=True)
    tm.assert_series_equal(result, expected)