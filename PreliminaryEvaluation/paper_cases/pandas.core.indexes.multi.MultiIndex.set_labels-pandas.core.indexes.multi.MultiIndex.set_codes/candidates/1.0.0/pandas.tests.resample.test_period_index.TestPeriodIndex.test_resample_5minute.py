@pytest.mark.parametrize('freq', ['5min'])
@pytest.mark.parametrize('kind', ['period', None, 'timestamp'])
def test_resample_5minute(self, freq, kind):
    rng = period_range('1/1/2000', '1/5/2000', freq='T')
    ts = Series(np.random.randn(len(rng)), index=rng)
    expected = ts.to_timestamp().resample(freq).mean()
    if kind != 'timestamp':
        expected = expected.to_period(freq)
    result = ts.resample(freq, kind=kind).mean()
    tm.assert_series_equal(result, expected)