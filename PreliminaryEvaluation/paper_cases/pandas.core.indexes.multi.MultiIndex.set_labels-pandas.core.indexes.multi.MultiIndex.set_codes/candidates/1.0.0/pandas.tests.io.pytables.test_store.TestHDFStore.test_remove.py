def test_remove(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        ts = tm.makeTimeSeries()
        df = tm.makeDataFrame()
        store['a'] = ts
        store['b'] = df
        _maybe_remove(store, 'a')
        assert len(store) == 1
        tm.assert_frame_equal(df, store['b'])
        _maybe_remove(store, 'b')
        assert len(store) == 0
        with pytest.raises(KeyError, match="'No object named a_nonexistent_store in the file'"):
            store.remove('a_nonexistent_store')
        store['a'] = ts
        store['b/foo'] = df
        _maybe_remove(store, 'foo')
        _maybe_remove(store, 'b/foo')
        assert len(store) == 1
        store['a'] = ts
        store['b/foo'] = df
        _maybe_remove(store, 'b')
        assert len(store) == 1
        store['a'] = ts
        store['b'] = df
        del store['a']
        del store['b']
        assert len(store) == 0