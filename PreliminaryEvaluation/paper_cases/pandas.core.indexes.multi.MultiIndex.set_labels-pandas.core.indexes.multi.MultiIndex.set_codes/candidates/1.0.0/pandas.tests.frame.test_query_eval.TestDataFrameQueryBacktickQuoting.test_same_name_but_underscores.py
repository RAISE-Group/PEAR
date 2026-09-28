def test_same_name_but_underscores(self, df):
    res = df.eval('C_C + `C C`')
    expect = df['C_C'] + df['C C']
    tm.assert_series_equal(res, expect)