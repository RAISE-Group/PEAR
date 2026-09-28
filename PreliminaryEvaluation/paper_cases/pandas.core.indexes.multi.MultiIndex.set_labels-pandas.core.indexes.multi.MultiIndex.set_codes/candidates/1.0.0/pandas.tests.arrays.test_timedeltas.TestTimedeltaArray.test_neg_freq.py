def test_neg_freq(self):
    tdi = pd.timedelta_range('2 Days', periods=4, freq='H')
    arr = TimedeltaArray(tdi, freq=tdi.freq)
    expected = TimedeltaArray(-tdi._data, freq=-tdi.freq)
    result = -arr
    tm.assert_timedelta_array_equal(result, expected)