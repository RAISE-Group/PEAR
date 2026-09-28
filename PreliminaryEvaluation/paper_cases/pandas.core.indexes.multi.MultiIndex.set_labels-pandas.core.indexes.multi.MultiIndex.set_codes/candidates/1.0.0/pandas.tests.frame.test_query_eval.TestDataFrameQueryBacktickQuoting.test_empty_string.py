def test_empty_string(self, df):
    res = df.query('`` > 5')
    expect = df[df[''] > 5]
    tm.assert_frame_equal(res, expect)