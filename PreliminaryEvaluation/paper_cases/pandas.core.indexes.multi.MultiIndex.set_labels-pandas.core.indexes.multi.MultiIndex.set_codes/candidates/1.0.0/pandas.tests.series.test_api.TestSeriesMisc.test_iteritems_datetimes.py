def test_iteritems_datetimes(self, datetime_series):
    for idx, val in datetime_series.iteritems():
        assert val == datetime_series[idx]