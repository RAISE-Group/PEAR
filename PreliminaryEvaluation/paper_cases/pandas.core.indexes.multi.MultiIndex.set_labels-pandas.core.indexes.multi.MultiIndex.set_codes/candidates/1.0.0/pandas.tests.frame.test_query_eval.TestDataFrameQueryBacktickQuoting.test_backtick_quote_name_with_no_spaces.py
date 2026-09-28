def test_backtick_quote_name_with_no_spaces(self, df):
    res = df.eval('A + `C_C`')
    expect = df['A'] + df['C_C']
    tm.assert_series_equal(res, expect)