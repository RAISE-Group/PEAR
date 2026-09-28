def test_pickle(self):

    def _check_roundtrip(obj):
        unpickled = tm.round_trip_pickle(obj)
        tm.assert_sp_array_equal(unpickled, obj)
    _check_roundtrip(self.arr)
    _check_roundtrip(self.zarr)