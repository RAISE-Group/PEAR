def test_chained_getitem_with_lists(self):

    def check(result, expected):
        tm.assert_numpy_array_equal(result, expected)
        assert isinstance(result, np.ndarray)
    df = DataFrame({'A': 5 * [np.zeros(3)], 'B': 5 * [np.ones(3)]})
    expected = df['A'].iloc[2]
    result = df.loc[2, 'A']
    check(result, expected)
    result2 = df.iloc[2]['A']
    check(result2, expected)
    result3 = df['A'].loc[2]
    check(result3, expected)
    result4 = df['A'].iloc[2]
    check(result4, expected)