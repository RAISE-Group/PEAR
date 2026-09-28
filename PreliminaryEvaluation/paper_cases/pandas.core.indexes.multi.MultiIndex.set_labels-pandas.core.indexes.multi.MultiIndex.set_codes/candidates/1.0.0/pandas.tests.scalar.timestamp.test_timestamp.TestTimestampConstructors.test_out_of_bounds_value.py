def test_out_of_bounds_value(self):
    one_us = np.timedelta64(1).astype('timedelta64[us]')
    min_ts_us = np.datetime64(Timestamp.min).astype('M8[us]')
    max_ts_us = np.datetime64(Timestamp.max).astype('M8[us]')
    Timestamp(min_ts_us)
    Timestamp(max_ts_us)
    with pytest.raises(ValueError):
        Timestamp(min_ts_us - one_us)
    with pytest.raises(ValueError):
        Timestamp(max_ts_us + one_us)