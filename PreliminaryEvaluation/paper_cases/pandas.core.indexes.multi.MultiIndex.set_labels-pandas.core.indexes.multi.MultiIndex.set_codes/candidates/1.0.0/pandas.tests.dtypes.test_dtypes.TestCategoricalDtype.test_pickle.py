def test_pickle(self):
    type(self.dtype).reset_cache()
    assert not len(self.dtype._cache)
    result = tm.round_trip_pickle(self.dtype)
    assert result == self.dtype