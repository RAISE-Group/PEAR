def test_crosstab_unsorted_order(self):
    df = pd.DataFrame({'b': [3, 1, 2], 'a': [5, 4, 6]}, index=['C', 'A', 'B'])
    result = pd.crosstab(df.index, [df.b, df.a])
    e_idx = pd.Index(['A', 'B', 'C'], name='row_0')
    e_columns = pd.MultiIndex.from_tuples([(1, 4), (2, 6), (3, 5)], names=['b', 'a'])
    expected = pd.DataFrame([[1, 0, 0], [0, 1, 0], [0, 0, 1]], index=e_idx, columns=e_columns)
    tm.assert_frame_equal(result, expected)