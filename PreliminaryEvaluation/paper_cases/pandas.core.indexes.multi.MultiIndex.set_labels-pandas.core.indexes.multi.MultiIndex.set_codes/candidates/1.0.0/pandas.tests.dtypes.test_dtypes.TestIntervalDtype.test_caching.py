def test_caching(self):
    IntervalDtype.reset_cache()
    dtype = IntervalDtype('int64')
    assert len(IntervalDtype._cache) == 1
    IntervalDtype('interval')
    assert len(IntervalDtype._cache) == 2
    IntervalDtype.reset_cache()
    tm.round_trip_pickle(dtype)
    assert len(IntervalDtype._cache) == 0