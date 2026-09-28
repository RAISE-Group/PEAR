def test_pickle(self, indices):
    original_name, indices.name = (indices.name, 'foo')
    unpickled = tm.round_trip_pickle(indices)
    assert indices.equals(unpickled)
    indices.name = original_name