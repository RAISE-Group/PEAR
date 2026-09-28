def test_already_underscore_variable(self, df):
    res = df.eval('`C_C` + A')
    expect = df['C_C'] + df['A']
    tm.assert_series_equal(res, expect)