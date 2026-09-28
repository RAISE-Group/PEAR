def test_detect_chained_assignment_warnings_filter_and_dupe_cols(self):
    with option_context('chained_assignment', 'warn'):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, -9]], columns=['a', 'a', 'c'])
        with tm.assert_produces_warning(com.SettingWithCopyWarning):
            df.c.loc[df.c > 0] = None
        expected = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, -9]], columns=['a', 'a', 'c'])
        tm.assert_frame_equal(df, expected)