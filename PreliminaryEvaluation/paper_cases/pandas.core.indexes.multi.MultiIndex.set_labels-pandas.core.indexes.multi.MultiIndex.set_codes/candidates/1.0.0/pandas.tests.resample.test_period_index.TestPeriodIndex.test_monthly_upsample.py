@pytest.mark.parametrize('target', ['D', 'B'])
@pytest.mark.parametrize('convention', ['start', 'end'])
def test_monthly_upsample(self, target, convention, simple_period_range_series):
    ts = simple_period_range_series('1/1/1990', '12/31/1995', freq='M')
    result = ts.resample(target, convention=convention).ffill()
    expected = result.to_timestamp(target, how=convention)
    expected = expected.asfreq(target, 'ffill').to_period()
    tm.assert_series_equal(result, expected)