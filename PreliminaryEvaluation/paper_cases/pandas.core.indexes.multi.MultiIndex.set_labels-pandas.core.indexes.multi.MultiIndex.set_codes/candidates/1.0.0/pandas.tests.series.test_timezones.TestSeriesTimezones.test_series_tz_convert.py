def test_series_tz_convert(self):
    rng = date_range('1/1/2011', periods=200, freq='D', tz='US/Eastern')
    ts = Series(1, index=rng)
    result = ts.tz_convert('Europe/Berlin')
    assert result.index.tz.zone == 'Europe/Berlin'
    rng = date_range('1/1/2011', periods=200, freq='D')
    ts = Series(1, index=rng)
    with pytest.raises(TypeError, match='Cannot convert tz-naive'):
        ts.tz_convert('US/Eastern')