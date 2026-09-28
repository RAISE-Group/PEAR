def test_keys(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        store['a'] = tm.makeTimeSeries()
        store['b'] = tm.makeStringSeries()
        store['c'] = tm.makeDataFrame()
        assert len(store) == 3
        expected = {'/a', '/b', '/c'}
        assert set(store.keys()) == expected
        assert set(store) == expected