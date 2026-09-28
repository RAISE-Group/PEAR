def test_multiple_spaces(self, df):
    res = df.query('`C  C` > 5')
    expect = df[df['C  C'] > 5]
    tm.assert_frame_equal(res, expect)