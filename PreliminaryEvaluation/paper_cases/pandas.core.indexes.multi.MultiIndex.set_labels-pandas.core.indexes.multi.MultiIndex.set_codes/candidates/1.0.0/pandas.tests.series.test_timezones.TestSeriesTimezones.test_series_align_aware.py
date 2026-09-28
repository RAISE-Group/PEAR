def test_series_align_aware(self):
    idx1 = date_range('2001', periods=5, freq='H', tz='US/Eastern')
    ser = Series(np.random.randn(len(idx1)), index=idx1)
    ser_central = ser.tz_convert('US/Central')
    new1, new2 = ser.align(ser_central)
    assert new1.index.tz == pytz.UTC
    assert new2.index.tz == pytz.UTC