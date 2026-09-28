def test_generic_errors(self, constructor):
    filler = self.get_kwargs_from_breaks(range(10))
    msg = "invalid option for 'closed': invalid"
    with pytest.raises(ValueError, match=msg):
        constructor(closed='invalid', **filler)
    msg = 'dtype must be an IntervalDtype, got int64'
    with pytest.raises(TypeError, match=msg):
        constructor(dtype='int64', **filler)
    msg = 'data type ["\']invalid["\'] not understood'
    with pytest.raises(TypeError, match=msg):
        constructor(dtype='invalid', **filler)
    periods = period_range('2000-01-01', periods=10)
    periods_kwargs = self.get_kwargs_from_breaks(periods)
    msg = 'Period dtypes are not supported, use a PeriodIndex instead'
    with pytest.raises(ValueError, match=msg):
        constructor(**periods_kwargs)
    decreasing_kwargs = self.get_kwargs_from_breaks(range(10, -1, -1))
    msg = 'left side of interval must be <= right side'
    with pytest.raises(ValueError, match=msg):
        constructor(**decreasing_kwargs)