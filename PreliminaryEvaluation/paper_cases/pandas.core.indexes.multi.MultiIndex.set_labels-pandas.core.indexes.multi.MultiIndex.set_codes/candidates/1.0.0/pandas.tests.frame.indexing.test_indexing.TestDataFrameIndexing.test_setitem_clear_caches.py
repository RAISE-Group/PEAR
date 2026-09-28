def test_setitem_clear_caches(self):
    df = DataFrame({'x': [1.1, 2.1, 3.1, 4.1], 'y': [5.1, 6.1, 7.1, 8.1]}, index=[0, 1, 2, 3])
    df.insert(2, 'z', np.nan)
    foo = df['z']
    df.loc[df.index[2:], 'z'] = 42
    expected = Series([np.nan, np.nan, 42, 42], index=df.index, name='z')
    assert df['z'] is not foo
    tm.assert_series_equal(df['z'], expected)