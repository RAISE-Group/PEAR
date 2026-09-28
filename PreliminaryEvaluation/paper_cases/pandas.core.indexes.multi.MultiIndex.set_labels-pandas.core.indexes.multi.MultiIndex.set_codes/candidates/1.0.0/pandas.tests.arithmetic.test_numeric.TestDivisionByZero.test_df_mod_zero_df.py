def test_df_mod_zero_df(self):
    df = pd.DataFrame({'first': [3, 4, 5, 8], 'second': [0, 0, 0, 3]})
    first = pd.Series([0, 0, 0, 0], dtype='float64')
    second = pd.Series([np.nan, np.nan, np.nan, 0])
    expected = pd.DataFrame({'first': first, 'second': second})
    result = df % df
    tm.assert_frame_equal(result, expected)