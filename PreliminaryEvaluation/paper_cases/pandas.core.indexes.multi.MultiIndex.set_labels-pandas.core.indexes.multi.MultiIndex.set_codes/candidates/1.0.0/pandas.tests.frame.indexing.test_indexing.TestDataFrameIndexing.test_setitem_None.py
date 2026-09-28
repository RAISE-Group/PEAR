def test_setitem_None(self, float_frame):
    float_frame[None] = float_frame['A']
    tm.assert_series_equal(float_frame.iloc[:, -1], float_frame['A'], check_names=False)
    tm.assert_series_equal(float_frame.loc[:, None], float_frame['A'], check_names=False)
    tm.assert_series_equal(float_frame[None], float_frame['A'], check_names=False)
    repr(float_frame)