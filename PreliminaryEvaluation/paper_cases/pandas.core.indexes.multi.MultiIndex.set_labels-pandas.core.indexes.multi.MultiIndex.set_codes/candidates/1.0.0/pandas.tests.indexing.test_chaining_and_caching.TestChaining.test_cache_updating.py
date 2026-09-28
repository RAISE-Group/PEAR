def test_cache_updating(self):
    df = tm.makeDataFrame()
    df['A']
    df.loc['Hello Friend'] = df.iloc[0]
    assert 'Hello Friend' in df['A'].index
    assert 'Hello Friend' in df['B'].index
    df = DataFrame(np.zeros((5, 5), dtype='int64'), columns=['a', 'b', 'c', 'd', 'e'], index=range(5))
    df['f'] = 0
    df.f.values[3] = 1
    df.f.values[3] = 2
    expected = DataFrame(np.zeros((5, 6), dtype='int64'), columns=['a', 'b', 'c', 'd', 'e', 'f'], index=range(5))
    expected.at[3, 'f'] = 2
    tm.assert_frame_equal(df, expected)
    expected = Series([0, 0, 0, 2, 0], name='f')
    tm.assert_series_equal(df.f, expected)