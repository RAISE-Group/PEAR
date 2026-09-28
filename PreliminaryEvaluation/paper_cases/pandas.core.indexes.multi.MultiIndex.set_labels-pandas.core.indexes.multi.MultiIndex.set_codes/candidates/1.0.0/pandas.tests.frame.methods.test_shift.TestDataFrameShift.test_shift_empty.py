def test_shift_empty(self):
    df = DataFrame({'foo': []})
    rs = df.shift(-1)
    tm.assert_frame_equal(df, rs)