def test_get(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        store['a'] = tm.makeTimeSeries()
        left = store.get('a')
        right = store['a']
        tm.assert_series_equal(left, right)
        left = store.get('/a')
        right = store['/a']
        tm.assert_series_equal(left, right)
        with pytest.raises(KeyError, match="'No object named b in the file'"):
            store.get('b')