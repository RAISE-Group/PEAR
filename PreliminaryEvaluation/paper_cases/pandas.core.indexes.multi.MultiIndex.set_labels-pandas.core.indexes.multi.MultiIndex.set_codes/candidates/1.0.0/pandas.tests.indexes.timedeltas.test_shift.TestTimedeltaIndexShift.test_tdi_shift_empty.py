def test_tdi_shift_empty(self):
    idx = pd.TimedeltaIndex([], name='xxx')
    tm.assert_index_equal(idx.shift(0, freq='H'), idx)
    tm.assert_index_equal(idx.shift(3, freq='H'), idx)