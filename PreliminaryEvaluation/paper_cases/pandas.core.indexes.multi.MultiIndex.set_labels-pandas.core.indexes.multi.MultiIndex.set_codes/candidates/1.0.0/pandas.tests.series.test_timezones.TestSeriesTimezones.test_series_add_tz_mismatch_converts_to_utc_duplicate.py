def test_series_add_tz_mismatch_converts_to_utc_duplicate(self):
    rng = date_range('1/1/2011', periods=10, freq='H', tz='US/Eastern')
    ser = Series(np.random.randn(len(rng)), index=rng)
    ts_moscow = ser.tz_convert('Europe/Moscow')
    result = ser + ts_moscow
    assert result.index.tz is pytz.utc
    result = ts_moscow + ser
    assert result.index.tz is pytz.utc