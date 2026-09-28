def test_series_add_aware_naive_raises(self):
    rng = date_range('1/1/2011', periods=10, freq='H')
    ser = Series(np.random.randn(len(rng)), index=rng)
    ser_utc = ser.tz_localize('utc')
    with pytest.raises(Exception):
        ser + ser_utc
    with pytest.raises(Exception):
        ser_utc + ser