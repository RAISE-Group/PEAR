def test_store_multiindex(self, setup_path):
    with ensure_clean_store(setup_path) as store:

        def make_index(names=None):
            return MultiIndex.from_tuples([(datetime.datetime(2013, 12, d), s, t) for d in range(1, 3) for s in range(2) for t in range(3)], names=names)
        _maybe_remove(store, 'df')
        df = DataFrame(np.zeros((12, 2)), columns=['a', 'b'], index=make_index())
        store.append('df', df)
        tm.assert_frame_equal(store.select('df'), df)
        _maybe_remove(store, 'df')
        df = DataFrame(np.zeros((12, 2)), columns=['a', 'b'], index=make_index(['date', None, None]))
        store.append('df', df)
        tm.assert_frame_equal(store.select('df'), df)
        _maybe_remove(store, 's')
        s = Series(np.zeros(12), index=make_index(['date', None, None]))
        store.append('s', s)
        xp = Series(np.zeros(12), index=make_index(['date', 'level_1', 'level_2']))
        tm.assert_series_equal(store.select('s'), xp)
        _maybe_remove(store, 'df')
        df = DataFrame(np.zeros((12, 2)), columns=['a', 'b'], index=make_index(['date', 'a', 't']))
        with pytest.raises(ValueError):
            store.append('df', df)
        _maybe_remove(store, 'df')
        df = DataFrame(np.zeros((12, 2)), columns=['a', 'b'], index=make_index(['date', 'date', 'date']))
        with pytest.raises(ValueError):
            store.append('df', df)
        _maybe_remove(store, 'df')
        df = DataFrame(np.zeros((12, 2)), columns=['a', 'b'], index=make_index(['date', 's', 't']))
        store.append('df', df)
        tm.assert_frame_equal(store.select('df'), df)