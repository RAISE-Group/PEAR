def test_keyword(self, df):
    res = df.eval('A + `def`')
    expect = df['A'] + df['def']
    tm.assert_series_equal(res, expect)