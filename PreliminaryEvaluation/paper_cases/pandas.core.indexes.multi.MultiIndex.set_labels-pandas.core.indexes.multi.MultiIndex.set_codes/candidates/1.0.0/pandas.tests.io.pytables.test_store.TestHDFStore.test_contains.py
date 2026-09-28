@ignore_natural_naming_warning
def test_contains(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        store['a'] = tm.makeTimeSeries()
        store['b'] = tm.makeDataFrame()
        store['foo/bar'] = tm.makeDataFrame()
        assert 'a' in store
        assert 'b' in store
        assert 'c' not in store
        assert 'foo/bar' in store
        assert '/foo/bar' in store
        assert '/foo/b' not in store
        assert 'bar' not in store
        with catch_warnings(record=True):
            store['node())'] = tm.makeDataFrame()
        assert 'node())' in store