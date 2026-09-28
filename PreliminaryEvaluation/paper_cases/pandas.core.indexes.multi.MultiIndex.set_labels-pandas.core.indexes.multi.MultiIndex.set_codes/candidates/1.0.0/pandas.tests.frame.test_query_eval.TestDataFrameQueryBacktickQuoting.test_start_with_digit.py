def test_start_with_digit(self, df):
    res = df.eval('A + `1e1`')
    expect = df['A'] + df['1e1']
    tm.assert_series_equal(res, expect)