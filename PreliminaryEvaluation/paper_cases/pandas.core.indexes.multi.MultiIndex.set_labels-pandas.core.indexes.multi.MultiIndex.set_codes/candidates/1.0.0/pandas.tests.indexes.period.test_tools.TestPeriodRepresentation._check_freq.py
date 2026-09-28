def _check_freq(self, freq, base_date):
    rng = period_range(start=base_date, periods=10, freq=freq)
    exp = np.arange(10, dtype=np.int64)
    tm.assert_numpy_array_equal(rng.asi8, exp)