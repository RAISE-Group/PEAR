def test_sort_values_stable_descending_multicolumn_sort(self):
    df = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]})
    expected = DataFrame({'A': [np.nan, 8, 6, 4, 2, 1, 1], 'B': [5, 4, 5, 5, np.nan, 2, 9]}, index=[2, 5, 4, 6, 1, 3, 0])
    sorted_df = df.sort_values(['A', 'B'], ascending=[0, 1], na_position='first', kind='mergesort')
    tm.assert_frame_equal(sorted_df, expected)
    expected = DataFrame({'A': [np.nan, 8, 6, 4, 2, 1, 1], 'B': [5, 4, 5, 5, np.nan, 9, 2]}, index=[2, 5, 4, 6, 1, 0, 3])
    sorted_df = df.sort_values(['A', 'B'], ascending=[0, 0], na_position='first', kind='mergesort')
    tm.assert_frame_equal(sorted_df, expected)