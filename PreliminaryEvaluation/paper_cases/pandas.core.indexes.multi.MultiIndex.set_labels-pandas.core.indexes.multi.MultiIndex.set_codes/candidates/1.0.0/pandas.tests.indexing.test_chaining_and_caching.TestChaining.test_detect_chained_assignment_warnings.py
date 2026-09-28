def test_detect_chained_assignment_warnings(self):
    with option_context('chained_assignment', 'warn'):
        df = DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
        with tm.assert_produces_warning(com.SettingWithCopyWarning):
            df.loc[0]['A'] = 111