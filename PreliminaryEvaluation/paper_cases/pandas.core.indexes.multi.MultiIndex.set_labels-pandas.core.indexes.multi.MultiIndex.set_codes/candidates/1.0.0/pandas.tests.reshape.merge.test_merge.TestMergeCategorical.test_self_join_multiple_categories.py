def test_self_join_multiple_categories(self):
    m = 5
    df = pd.DataFrame({'a': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] * m, 'b': ['t', 'w', 'x', 'y', 'z'] * 2 * m, 'c': [letter for each in ['m', 'n', 'u', 'p', 'o'] for letter in [each] * 2 * m], 'd': [letter for each in ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj'] for letter in [each] * m]})
    df = df.apply(lambda x: x.astype('category'))
    result = pd.merge(df, df, on=list(df.columns))
    tm.assert_frame_equal(result, df)