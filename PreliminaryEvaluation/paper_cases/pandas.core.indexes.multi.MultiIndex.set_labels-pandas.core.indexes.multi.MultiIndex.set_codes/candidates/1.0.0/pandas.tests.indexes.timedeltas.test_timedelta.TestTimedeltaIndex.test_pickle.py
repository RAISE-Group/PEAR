def test_pickle(self):
    rng = timedelta_range('1 days', periods=10)
    rng_p = tm.round_trip_pickle(rng)
    tm.assert_index_equal(rng, rng_p)