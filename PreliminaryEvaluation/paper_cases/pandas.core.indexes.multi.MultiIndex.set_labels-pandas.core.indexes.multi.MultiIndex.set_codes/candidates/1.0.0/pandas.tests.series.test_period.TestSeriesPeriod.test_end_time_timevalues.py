@pytest.mark.parametrize('input_vals', [[Period('2016-01', freq='M'), Period('2016-02', freq='M')], [Period('2016-01-01', freq='D'), Period('2016-01-02', freq='D')], [Period('2016-01-01 00:00:00', freq='H'), Period('2016-01-01 01:00:00', freq='H')], [Period('2016-01-01 00:00:00', freq='M'), Period('2016-01-01 00:01:00', freq='M')], [Period('2016-01-01 00:00:00', freq='S'), Period('2016-01-01 00:00:01', freq='S')]])
def test_end_time_timevalues(self, input_vals):
    input_vals = PeriodArray._from_sequence(np.asarray(input_vals))
    s = Series(input_vals)
    result = s.dt.end_time
    expected = s.apply(lambda x: x.end_time)
    tm.assert_series_equal(result, expected)