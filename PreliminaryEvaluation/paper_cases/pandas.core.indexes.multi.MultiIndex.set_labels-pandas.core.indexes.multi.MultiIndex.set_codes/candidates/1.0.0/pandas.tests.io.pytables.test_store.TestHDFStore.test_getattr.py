def test_getattr(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        s = tm.makeTimeSeries()
        store['a'] = s
        result = store.a
        tm.assert_series_equal(result, s)
        result = getattr(store, 'a')
        tm.assert_series_equal(result, s)
        df = tm.makeTimeDataFrame()
        store['df'] = df
        result = store.df
        tm.assert_frame_equal(result, df)
        for x in ['d', 'mode', 'path', 'handle', 'complib']:
            with pytest.raises(AttributeError):
                getattr(store, x)
        for x in ['mode', 'path', 'handle', 'complib']:
            getattr(store, '_{x}'.format(x=x))