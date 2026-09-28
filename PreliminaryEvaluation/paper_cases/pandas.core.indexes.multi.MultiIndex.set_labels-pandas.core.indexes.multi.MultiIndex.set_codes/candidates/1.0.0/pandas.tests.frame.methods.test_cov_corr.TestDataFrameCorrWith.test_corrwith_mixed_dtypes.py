def test_corrwith_mixed_dtypes(self):
    df = pd.DataFrame({'a': [1, 4, 3, 2], 'b': [4, 6, 7, 3], 'c': ['a', 'b', 'c', 'd']})
    s = pd.Series([0, 6, 7, 3])
    result = df.corrwith(s)
    corrs = [df['a'].corr(s), df['b'].corr(s)]
    expected = pd.Series(data=corrs, index=['a', 'b'])
    tm.assert_series_equal(result, expected)