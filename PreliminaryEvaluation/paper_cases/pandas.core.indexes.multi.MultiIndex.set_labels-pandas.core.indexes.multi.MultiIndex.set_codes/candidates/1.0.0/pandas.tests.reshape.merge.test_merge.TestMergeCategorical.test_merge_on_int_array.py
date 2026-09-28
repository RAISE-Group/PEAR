def test_merge_on_int_array(self):
    df = pd.DataFrame({'A': pd.Series([1, 2, np.nan], dtype='Int64'), 'B': 1})
    result = pd.merge(df, df, on='A')
    expected = pd.DataFrame({'A': pd.Series([1, 2, np.nan], dtype='Int64'), 'B_x': 1, 'B_y': 1})
    tm.assert_frame_equal(result, expected)