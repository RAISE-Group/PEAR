def test_dataframe_utc_true(self):
    df = pd.DataFrame({'year': [2015, 2016], 'month': [2, 3], 'day': [4, 5]})
    result = pd.to_datetime(df, utc=True)
    expected = pd.Series(np.array(['2015-02-04', '2016-03-05'], dtype='datetime64[ns]')).dt.tz_localize('UTC')
    tm.assert_series_equal(result, expected)