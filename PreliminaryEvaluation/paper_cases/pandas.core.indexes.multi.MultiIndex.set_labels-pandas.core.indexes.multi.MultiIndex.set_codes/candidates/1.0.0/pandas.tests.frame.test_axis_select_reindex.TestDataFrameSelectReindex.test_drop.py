def test_drop(self):
    simple = DataFrame({'A': [1, 2, 3, 4], 'B': [0, 1, 2, 3]})
    tm.assert_frame_equal(simple.drop('A', axis=1), simple[['B']])
    tm.assert_frame_equal(simple.drop(['A', 'B'], axis='columns'), simple[[]])
    tm.assert_frame_equal(simple.drop([0, 1, 3], axis=0), simple.loc[[2], :])
    tm.assert_frame_equal(simple.drop([0, 3], axis='index'), simple.loc[[1, 2], :])
    with pytest.raises(KeyError, match='\\[5\\] not found in axis'):
        simple.drop(5)
    with pytest.raises(KeyError, match="\\['C'\\] not found in axis"):
        simple.drop('C', 1)
    with pytest.raises(KeyError, match='\\[5\\] not found in axis'):
        simple.drop([1, 5])
    with pytest.raises(KeyError, match="\\['C'\\] not found in axis"):
        simple.drop(['A', 'C'], 1)
    tm.assert_frame_equal(simple.drop(5, errors='ignore'), simple)
    tm.assert_frame_equal(simple.drop([0, 5], errors='ignore'), simple.loc[[1, 2, 3], :])
    tm.assert_frame_equal(simple.drop('C', axis=1, errors='ignore'), simple)
    tm.assert_frame_equal(simple.drop(['A', 'C'], axis=1, errors='ignore'), simple[['B']])
    nu_df = DataFrame(list(zip(range(3), range(-3, 1), list('abc'))), columns=['a', 'a', 'b'])
    tm.assert_frame_equal(nu_df.drop('a', axis=1), nu_df[['b']])
    tm.assert_frame_equal(nu_df.drop('b', axis='columns'), nu_df['a'])
    tm.assert_frame_equal(nu_df.drop([]), nu_df)
    nu_df = nu_df.set_index(pd.Index(['X', 'Y', 'X']))
    nu_df.columns = list('abc')
    tm.assert_frame_equal(nu_df.drop('X', axis='rows'), nu_df.loc[['Y'], :])
    tm.assert_frame_equal(nu_df.drop(['X', 'Y'], axis=0), nu_df.loc[[], :])
    df = pd.DataFrame(np.random.randn(10, 3), columns=list('abc'))
    expected = df[~(df.b > 0)]
    df.drop(labels=df[df.b > 0].index, inplace=True)
    tm.assert_frame_equal(df, expected)