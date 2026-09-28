def test_groupby_max_datetime64(self):
    df = DataFrame(dict(A=Timestamp('20130101'), B=np.arange(5)))
    expected = df.groupby('A')['A'].apply(lambda x: x.max())
    result = df.groupby('A')['A'].max()
    tm.assert_series_equal(result, expected)