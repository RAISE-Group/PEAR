@pytest.mark.parametrize('rule,expected_error_msg', [('a-dec', '<YearEnd: month=12>'), ('q-mar', '<QuarterEnd: startingMonth=3>'), ('M', '<MonthEnd>'), ('w-thu', '<Week: weekday=3>')])
def test_not_subperiod(self, simple_period_range_series, rule, expected_error_msg):
    ts = simple_period_range_series('1/1/1990', '6/30/1995', freq='w-wed')
    msg = 'Frequency <Week: weekday=2> cannot be resampled to {}, as they are not sub or super periods'.format(expected_error_msg)
    with pytest.raises(IncompatibleFrequency, match=msg):
        ts.resample(rule).mean()