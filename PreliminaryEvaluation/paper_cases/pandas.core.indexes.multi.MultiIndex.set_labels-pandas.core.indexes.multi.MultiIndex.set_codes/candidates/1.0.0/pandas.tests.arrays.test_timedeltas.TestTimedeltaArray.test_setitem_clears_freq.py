def test_setitem_clears_freq(self):
    a = TimedeltaArray(pd.timedelta_range('1H', periods=2, freq='H'))
    a[0] = pd.Timedelta('1H')
    assert a.freq is None