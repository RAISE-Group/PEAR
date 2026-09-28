def test_setting_with_copy_bug(self):
    df = DataFrame({'a': list(range(4)), 'b': list('ab..'), 'c': ['a', 'b', np.nan, 'd']})
    mask = pd.isna(df.c)
    msg = 'A value is trying to be set on a copy of a slice from a DataFrame'
    with pytest.raises(com.SettingWithCopyError, match=msg):
        df[['c']][mask] = df[['b']][mask]
    df1 = DataFrame({'x': Series(['a', 'b', 'c']), 'y': Series(['d', 'e', 'f'])})
    df2 = df1[['x']]
    df2['y'] = ['g', 'h', 'i']