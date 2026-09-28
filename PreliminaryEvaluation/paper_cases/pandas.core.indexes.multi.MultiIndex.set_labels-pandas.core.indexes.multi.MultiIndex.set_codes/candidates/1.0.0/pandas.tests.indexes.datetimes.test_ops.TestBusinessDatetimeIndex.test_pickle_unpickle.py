def test_pickle_unpickle(self):
    unpickled = tm.round_trip_pickle(self.rng)
    assert unpickled.freq is not None