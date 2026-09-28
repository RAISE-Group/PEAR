def test_setitem_tuple(self, float_frame):
    float_frame['A', 'B'] = float_frame['A']
    tm.assert_series_equal(float_frame['A', 'B'], float_frame['A'], check_names=False)