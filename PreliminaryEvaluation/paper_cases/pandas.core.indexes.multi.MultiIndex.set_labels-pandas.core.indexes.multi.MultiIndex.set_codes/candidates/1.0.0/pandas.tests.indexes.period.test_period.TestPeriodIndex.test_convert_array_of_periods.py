def test_convert_array_of_periods(self):
    rng = period_range('1/1/2000', periods=20, freq='D')
    periods = list(rng)
    result = pd.Index(periods)
    assert isinstance(result, PeriodIndex)