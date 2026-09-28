def test_two_backtick_variables_expr(self, df):
    res = df.eval('`B B` + `C C`')
    expect = df['B B'] + df['C C']
    tm.assert_series_equal(res, expect)