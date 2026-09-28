def test_df_div_zero_df(self):
    df = pd.DataFrame({'first': [3, 4, 5, 8], 'second': [0, 0, 0, 3]})
    result = df / df
    first = pd.Series([1.0, 1.0, 1.0, 1.0])
    second = pd.Series([np.nan, np.nan, np.nan, 1])
    expected = pd.DataFrame({'first': first, 'second': second})
    tm.assert_frame_equal(result, expected)