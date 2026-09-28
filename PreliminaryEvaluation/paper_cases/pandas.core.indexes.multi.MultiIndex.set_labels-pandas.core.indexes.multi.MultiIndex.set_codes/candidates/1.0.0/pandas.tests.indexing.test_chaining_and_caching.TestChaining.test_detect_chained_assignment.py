def test_detect_chained_assignment(self):
    pd.set_option('chained_assignment', 'raise')
    expected = DataFrame([[-5, 1], [-6, 3]], columns=list('AB'))
    df = DataFrame(np.arange(4).reshape(2, 2), columns=list('AB'), dtype='int64')
    assert df._is_copy is None
    df['A'][0] = -5
    df['A'][1] = -6
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'A': Series(range(2), dtype='int64'), 'B': np.array(np.arange(2, 4), dtype=np.float64)})
    assert df._is_copy is None
    with pytest.raises(com.SettingWithCopyError):
        df['A'][0] = -5
    with pytest.raises(com.SettingWithCopyError):
        df['A'][1] = np.nan
    assert df['A']._is_copy is None
    df = DataFrame({'A': Series(range(2), dtype='int64'), 'B': np.array(np.arange(2, 4), dtype=np.float64)})
    with pytest.raises(com.SettingWithCopyError):
        df.loc[0]['A'] = -5
    df = DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'], 'c': Series(range(7), dtype='int64')})
    assert df._is_copy is None
    with pytest.raises(com.SettingWithCopyError):
        indexer = df.a.str.startswith('o')
        df[indexer]['c'] = 42
    expected = DataFrame({'A': [111, 'bbb', 'ccc'], 'B': [1, 2, 3]})
    df = DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
    with pytest.raises(com.SettingWithCopyError):
        df['A'][0] = 111
    with pytest.raises(com.SettingWithCopyError):
        df.loc[0]['A'] = 111
    df.loc[0, 'A'] = 111
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'A': [1, 2]})
    assert df._is_copy is None
    with tm.ensure_clean('__tmp__pickle') as path:
        df.to_pickle(path)
        df2 = pd.read_pickle(path)
        df2['B'] = df2['A']
        df2['B'] = df2['A']
    from string import ascii_letters as letters

    def random_text(nobs=100):
        df = []
        for i in range(nobs):
            idx = np.random.randint(len(letters), size=2)
            idx.sort()
            df.append([letters[idx[0]:idx[1]]])
        return DataFrame(df, columns=['letters'])
    df = random_text(100000)
    x = df.iloc[[0, 1, 2]]
    assert x._is_copy is not None
    x = df.iloc[[0, 1, 2, 4]]
    assert x._is_copy is not None
    indexer = df.letters.apply(lambda x: len(x) > 10)
    df = df.loc[indexer].copy()
    assert df._is_copy is None
    df['letters'] = df['letters'].apply(str.lower)
    df = random_text(100000)
    indexer = df.letters.apply(lambda x: len(x) > 10)
    df = df.loc[indexer]
    assert df._is_copy is not None
    df['letters'] = df['letters'].apply(str.lower)
    df = random_text(100000)
    indexer = df.letters.apply(lambda x: len(x) > 10)
    df = df.loc[indexer]
    assert df._is_copy is not None
    df.loc[:, 'letters'] = df['letters'].apply(str.lower)
    assert df._is_copy is None
    df['letters'] = df['letters'].apply(str.lower)
    assert df._is_copy is None
    df = random_text(100000)
    indexer = df.letters.apply(lambda x: len(x) > 10)
    df.loc[indexer, 'letters'] = df.loc[indexer, 'letters'].apply(str.lower)
    df = DataFrame({'a': [1]}).dropna()
    assert df._is_copy is None
    df['a'] += 1
    df = DataFrame(np.random.randn(10, 4))
    s = df.iloc[:, 0].sort_values()
    tm.assert_series_equal(s, df.iloc[:, 0].sort_values())
    tm.assert_series_equal(s, df[0].sort_values())
    df = DataFrame({'column1': ['a', 'a', 'a'], 'column2': [4, 8, 9]})
    str(df)
    df['column1'] = df['column1'] + 'b'
    str(df)
    df = df[df['column2'] != 8]
    str(df)
    df['column1'] = df['column1'] + 'c'
    str(df)
    df = DataFrame(np.arange(0, 9), columns=['count'])
    df['group'] = 'b'
    with pytest.raises(com.SettingWithCopyError):
        df.iloc[0:5]['group'] = 'a'
    df = DataFrame(dict(A=date_range('20130101', periods=5), B=np.random.randn(5), C=np.arange(5, dtype='int64'), D=list('abcde')))
    with pytest.raises(com.SettingWithCopyError):
        df.loc[2]['D'] = 'foo'
    with pytest.raises(com.SettingWithCopyError):
        df.loc[2]['C'] = 'foo'
    with pytest.raises(com.SettingWithCopyError):
        df['C'][2] = 'foo'