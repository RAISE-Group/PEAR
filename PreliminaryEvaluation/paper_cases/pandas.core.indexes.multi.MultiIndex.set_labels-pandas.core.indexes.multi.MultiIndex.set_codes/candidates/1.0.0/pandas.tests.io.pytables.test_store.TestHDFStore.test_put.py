def test_put(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        ts = tm.makeTimeSeries()
        df = tm.makeTimeDataFrame()
        store['a'] = ts
        store['b'] = df[:10]
        store['foo/bar/bah'] = df[:10]
        store['foo'] = df[:10]
        store['/foo'] = df[:10]
        store.put('c', df[:10], format='table')
        with pytest.raises(ValueError):
            store.put('b', df[10:], append=True)
        _maybe_remove(store, 'f')
        with pytest.raises(ValueError):
            store.put('f', df[10:], append=True)
        with pytest.raises(ValueError):
            store.put('c', df[10:], append=True)
        store.put('c', df[:10], format='table', append=False)
        tm.assert_frame_equal(df[:10], store['c'])