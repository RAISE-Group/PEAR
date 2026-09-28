def test_frame_tz_convert(self):
    rng = date_range('1/1/2011', periods=200, freq='D', tz='US/Eastern')
    df = DataFrame({'a': 1}, index=rng)
    result = df.tz_convert('Europe/Berlin')
    expected = DataFrame({'a': 1}, rng.tz_convert('Europe/Berlin'))
    assert result.index.tz.zone == 'Europe/Berlin'
    tm.assert_frame_equal(result, expected)
    df = df.T
    result = df.tz_convert('Europe/Berlin', axis=1)
    assert result.columns.tz.zone == 'Europe/Berlin'
    tm.assert_frame_equal(result, expected.T)