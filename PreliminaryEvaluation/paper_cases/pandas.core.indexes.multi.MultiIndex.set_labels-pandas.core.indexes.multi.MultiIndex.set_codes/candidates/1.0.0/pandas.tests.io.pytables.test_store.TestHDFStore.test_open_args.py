def test_open_args(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        store = HDFStore(path, mode='a', driver='H5FD_CORE', driver_core_backing_store=0)
        store['df'] = df
        store.append('df2', df)
        tm.assert_frame_equal(store['df'], df)
        tm.assert_frame_equal(store['df2'], df)
        store.close()
        assert not os.path.exists(path)