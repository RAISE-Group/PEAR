def test_tdi_shift_minutes(self):
    idx = pd.TimedeltaIndex(['5 hours', '6 hours', '9 hours'], name='xxx')
    tm.assert_index_equal(idx.shift(0, freq='T'), idx)
    exp = pd.TimedeltaIndex(['05:03:00', '06:03:00', '9:03:00'], name='xxx')
    tm.assert_index_equal(idx.shift(3, freq='T'), exp)
    exp = pd.TimedeltaIndex(['04:57:00', '05:57:00', '8:57:00'], name='xxx')
    tm.assert_index_equal(idx.shift(-3, freq='T'), exp)