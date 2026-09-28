def test_start_with_spaces(self, df):
    res = df.eval('` A` + `  `')
    expect = df[' A'] + df['  ']
    tm.assert_series_equal(res, expect)