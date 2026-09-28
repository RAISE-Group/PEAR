def test_put_compression(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = tm.makeTimeDataFrame()
        store.put('c', df, format='table', complib='zlib')
        tm.assert_frame_equal(store['c'], df)
        with pytest.raises(ValueError):
            store.put('b', df, format='fixed', complib='zlib')