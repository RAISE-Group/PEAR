def test_isin_against_series(self):
    df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]}, index=['a', 'b', 'c', 'd'])
    s = pd.Series([1, 3, 11, 4], index=['a', 'b', 'c', 'd'])
    expected = DataFrame(False, index=df.index, columns=df.columns)
    expected['A'].loc['a'] = True
    expected.loc['d'] = True
    result = df.isin(s)
    tm.assert_frame_equal(result, expected)