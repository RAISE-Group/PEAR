def test_timeseries_coercion(self):
    idx = tm.makeDateIndex(10000)
    ser = Series(np.random.randn(len(idx)), idx.astype(object))
    assert ser.index.is_all_dates
    assert isinstance(ser.index, DatetimeIndex)