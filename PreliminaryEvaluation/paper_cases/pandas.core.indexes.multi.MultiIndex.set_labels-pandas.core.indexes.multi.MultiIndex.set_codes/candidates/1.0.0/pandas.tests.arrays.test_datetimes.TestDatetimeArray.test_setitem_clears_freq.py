def test_setitem_clears_freq(self):
    a = DatetimeArray(pd.date_range('2000', periods=2, freq='D', tz='US/Central'))
    a[0] = pd.Timestamp('2000', tz='US/Central')
    assert a.freq is None