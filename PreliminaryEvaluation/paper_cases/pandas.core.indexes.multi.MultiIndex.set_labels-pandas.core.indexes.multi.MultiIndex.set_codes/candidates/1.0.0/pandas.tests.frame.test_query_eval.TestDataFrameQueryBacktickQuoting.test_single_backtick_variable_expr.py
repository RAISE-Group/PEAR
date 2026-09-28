def test_single_backtick_variable_expr(self, df):
    res = df.eval('A + `B B`')
    expect = df['A'] + df['B B']
    tm.assert_series_equal(res, expect)