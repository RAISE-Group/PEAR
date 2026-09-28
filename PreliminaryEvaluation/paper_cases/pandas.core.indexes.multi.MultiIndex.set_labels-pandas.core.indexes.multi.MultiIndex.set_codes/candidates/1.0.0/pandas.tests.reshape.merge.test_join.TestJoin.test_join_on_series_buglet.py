def test_join_on_series_buglet(self):
    df = DataFrame({'a': [1, 1]})
    ds = Series([2], index=[1], name='b')
    result = df.join(ds, on='a')
    expected = DataFrame({'a': [1, 1], 'b': [2, 2]}, index=df.index)
    tm.assert_frame_equal(result, expected)