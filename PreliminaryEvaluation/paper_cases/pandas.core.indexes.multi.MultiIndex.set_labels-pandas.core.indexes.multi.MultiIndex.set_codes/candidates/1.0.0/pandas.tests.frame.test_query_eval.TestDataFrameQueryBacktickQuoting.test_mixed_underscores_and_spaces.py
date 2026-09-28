def test_mixed_underscores_and_spaces(self, df):
    res = df.eval('A + `D_D D`')
    expect = df['A'] + df['D_D D']
    tm.assert_series_equal(res, expect)