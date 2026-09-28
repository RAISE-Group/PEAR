def test_unneeded_quoting(self, df):
    res = df.query('`A` > 2')
    expect = df[df['A'] > 2]
    tm.assert_frame_equal(res, expect)