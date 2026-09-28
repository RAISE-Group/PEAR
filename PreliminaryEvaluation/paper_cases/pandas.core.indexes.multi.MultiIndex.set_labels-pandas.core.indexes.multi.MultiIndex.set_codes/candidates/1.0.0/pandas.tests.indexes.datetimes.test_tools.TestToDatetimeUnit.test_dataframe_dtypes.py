@pytest.mark.parametrize('cache', [True, False])
def test_dataframe_dtypes(self, cache):
    df = DataFrame({'year': [2015, 2016], 'month': [2, 3], 'day': [4, 5]})
    result = to_datetime(df.astype('int16'), cache=cache)
    expected = Series([Timestamp('20150204 00:00:00'), Timestamp('20160305 00:00:00')])
    tm.assert_series_equal(result, expected)
    df['month'] = df['month'].astype('int8')
    df['day'] = df['day'].astype('int8')
    result = to_datetime(df, cache=cache)
    expected = Series([Timestamp('20150204 00:00:00'), Timestamp('20160305 00:00:00')])
    tm.assert_series_equal(result, expected)
    df = DataFrame({'year': [2000, 2001], 'month': [1.5, 1], 'day': [1, 1]})
    with pytest.raises(ValueError):
        to_datetime(df, cache=cache)