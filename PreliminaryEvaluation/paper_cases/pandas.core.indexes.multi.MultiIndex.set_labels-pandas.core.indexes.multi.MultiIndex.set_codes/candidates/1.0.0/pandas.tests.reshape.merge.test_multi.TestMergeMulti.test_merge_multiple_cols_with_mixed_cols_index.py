def test_merge_multiple_cols_with_mixed_cols_index(self):
    s = pd.Series(range(6), pd.MultiIndex.from_product([['A', 'B'], [1, 2, 3]], names=['lev1', 'lev2']), name='Amount')
    df = pd.DataFrame({'lev1': list('AAABBB'), 'lev2': [1, 2, 3, 1, 2, 3], 'col': 0})
    result = pd.merge(df, s.reset_index(), on=['lev1', 'lev2'])
    expected = pd.DataFrame({'lev1': list('AAABBB'), 'lev2': [1, 2, 3, 1, 2, 3], 'col': [0] * 6, 'Amount': range(6)})
    tm.assert_frame_equal(result, expected)