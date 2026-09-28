def test_resample_fill_missing(self):
    rng = PeriodIndex([2000, 2005, 2007, 2009], freq='A')
    s = Series(np.random.randn(4), index=rng)
    stamps = s.to_timestamp()
    filled = s.resample('A').ffill()
    expected = stamps.resample('A').ffill().to_period('A')
    tm.assert_series_equal(filled, expected)