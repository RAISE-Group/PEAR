def test_with_dictlike_columns(self):
    df = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    result = df.apply(lambda x: {'s': x['a'] + x['b']}, axis=1)
    expected = Series([{'s': 3} for t in df.itertuples()])
    tm.assert_series_equal(result, expected)
    df['tm'] = [pd.Timestamp('2017-05-01 00:00:00'), pd.Timestamp('2017-05-02 00:00:00')]
    result = df.apply(lambda x: {'s': x['a'] + x['b']}, axis=1)
    tm.assert_series_equal(result, expected)
    result = (df['a'] + df['b']).apply(lambda x: {'s': x})
    expected = Series([{'s': 3}, {'s': 3}])
    tm.assert_series_equal(result, expected)
    df = DataFrame()
    df['author'] = ['X', 'Y', 'Z']
    df['publisher'] = ['BBC', 'NBC', 'N24']
    df['date'] = pd.to_datetime(['17-10-2010 07:15:30', '13-05-2011 08:20:35', '15-01-2013 09:09:09'])
    result = df.apply(lambda x: {}, axis=1)
    expected = Series([{}, {}, {}])
    tm.assert_series_equal(result, expected)