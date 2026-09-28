def test_tdi_shift_hours(self):
    idx = pd.TimedeltaIndex(['5 hours', '6 hours', '9 hours'], name='xxx')
    tm.assert_index_equal(idx.shift(0, freq='H'), idx)
    exp = pd.TimedeltaIndex(['8 hours', '9 hours', '12 hours'], name='xxx')
    tm.assert_index_equal(idx.shift(3, freq='H'), exp)
    exp = pd.TimedeltaIndex(['2 hours', '3 hours', '6 hours'], name='xxx')
    tm.assert_index_equal(idx.shift(-3, freq='H'), exp)