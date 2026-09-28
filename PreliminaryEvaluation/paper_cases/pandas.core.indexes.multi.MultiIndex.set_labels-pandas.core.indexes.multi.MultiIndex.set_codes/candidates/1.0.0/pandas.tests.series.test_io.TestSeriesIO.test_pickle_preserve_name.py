def test_pickle_preserve_name(self):
    for n in [777, 777.0, 'name', datetime(2001, 11, 11), (1, 2)]:
        unpickled = self._pickle_roundtrip_name(tm.makeTimeSeries(name=n))
        assert unpickled.name == n