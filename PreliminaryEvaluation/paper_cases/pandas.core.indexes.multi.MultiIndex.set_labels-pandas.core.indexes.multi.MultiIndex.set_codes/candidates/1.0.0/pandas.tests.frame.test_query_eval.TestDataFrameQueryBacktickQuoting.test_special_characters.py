def test_special_characters(self, df):
    res = df.eval('`E.E` + `F-F` - A')
    expect = df['E.E'] + df['F-F'] - df['A']
    tm.assert_series_equal(res, expect)