def test_interpolate_time_raises_for_non_timeseries(self):
    non_ts = Series([0, 1, 2, np.NaN])
    msg = 'time-weighted interpolation only works on Series.* with a DatetimeIndex'
    with pytest.raises(ValueError, match=msg):
        non_ts.interpolate(method='time')