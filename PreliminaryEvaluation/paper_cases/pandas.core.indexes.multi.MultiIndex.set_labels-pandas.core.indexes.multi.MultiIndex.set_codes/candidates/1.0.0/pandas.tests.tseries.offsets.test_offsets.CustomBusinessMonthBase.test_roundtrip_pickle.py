def test_roundtrip_pickle(self):

    def _check_roundtrip(obj):
        unpickled = tm.round_trip_pickle(obj)
        assert unpickled == obj
    _check_roundtrip(self._offset())
    _check_roundtrip(self._offset(2))
    _check_roundtrip(self._offset() * 2)