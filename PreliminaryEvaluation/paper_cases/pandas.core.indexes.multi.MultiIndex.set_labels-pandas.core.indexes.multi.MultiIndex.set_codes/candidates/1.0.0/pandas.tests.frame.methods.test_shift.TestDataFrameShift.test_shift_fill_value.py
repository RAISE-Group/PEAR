def test_shift_fill_value(self):
    df = DataFrame([1, 2, 3, 4, 5], index=date_range('1/1/2000', periods=5, freq='H'))
    exp = DataFrame([0, 1, 2, 3, 4], index=date_range('1/1/2000', periods=5, freq='H'))
    result = df.shift(1, fill_value=0)
    tm.assert_frame_equal(result, exp)
    exp = DataFrame([0, 0, 1, 2, 3], index=date_range('1/1/2000', periods=5, freq='H'))
    result = df.shift(2, fill_value=0)
    tm.assert_frame_equal(result, exp)