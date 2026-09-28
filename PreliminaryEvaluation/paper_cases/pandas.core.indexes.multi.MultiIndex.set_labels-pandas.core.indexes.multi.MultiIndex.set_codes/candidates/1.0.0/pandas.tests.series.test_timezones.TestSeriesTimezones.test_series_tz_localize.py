def test_series_tz_localize(self):
    rng = date_range('1/1/2011', periods=100, freq='H')
    ts = Series(1, index=rng)
    result = ts.tz_localize('utc')
    assert result.index.tz.zone == 'UTC'
    rng = date_range('1/1/2011', periods=100, freq='H', tz='utc')
    ts = Series(1, index=rng)
    with pytest.raises(TypeError, match='Already tz-aware'):
        ts.tz_localize('US/Eastern')