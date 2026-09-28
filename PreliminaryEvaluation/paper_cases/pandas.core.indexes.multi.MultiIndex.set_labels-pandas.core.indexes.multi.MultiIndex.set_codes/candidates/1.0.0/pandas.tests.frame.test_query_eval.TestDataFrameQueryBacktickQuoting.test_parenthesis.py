def test_parenthesis(self, df):
    res = df.query('`A (x)` > 2')
    expect = df[df['A (x)'] > 2]
    tm.assert_frame_equal(res, expect)