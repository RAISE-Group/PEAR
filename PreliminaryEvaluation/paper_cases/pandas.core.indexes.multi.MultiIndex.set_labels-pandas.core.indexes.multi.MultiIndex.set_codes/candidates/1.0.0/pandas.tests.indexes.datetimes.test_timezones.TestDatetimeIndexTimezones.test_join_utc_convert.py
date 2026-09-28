def test_join_utc_convert(self, join_type):
    rng = date_range('1/1/2011', periods=100, freq='H', tz='utc')
    left = rng.tz_convert('US/Eastern')
    right = rng.tz_convert('Europe/Berlin')
    result = left.join(left[:-5], how=join_type)
    assert isinstance(result, DatetimeIndex)
    assert result.tz == left.tz
    result = left.join(right[:-5], how=join_type)
    assert isinstance(result, DatetimeIndex)
    assert result.tz.zone == 'UTC'