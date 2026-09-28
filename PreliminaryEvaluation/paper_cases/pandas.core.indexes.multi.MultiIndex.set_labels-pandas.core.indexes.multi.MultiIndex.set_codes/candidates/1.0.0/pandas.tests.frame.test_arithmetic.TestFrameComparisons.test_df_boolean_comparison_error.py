def test_df_boolean_comparison_error(self):
    df = pd.DataFrame(np.arange(6).reshape((3, 2)))
    expected = pd.DataFrame([[False, False], [True, False], [False, False]])
    result = df == (2, 2)
    tm.assert_frame_equal(result, expected)
    result = df == [2, 2]
    tm.assert_frame_equal(result, expected)