def test_tdi_mul_int_series(self, box_with_array):
    box = box_with_array
    xbox = pd.Series if box in [pd.Index, tm.to_array] else box
    idx = TimedeltaIndex(np.arange(5, dtype='int64'))
    expected = TimedeltaIndex(np.arange(5, dtype='int64') ** 2)
    idx = tm.box_expected(idx, box)
    expected = tm.box_expected(expected, xbox)
    result = idx * pd.Series(np.arange(5, dtype='int64'))
    tm.assert_equal(result, expected)