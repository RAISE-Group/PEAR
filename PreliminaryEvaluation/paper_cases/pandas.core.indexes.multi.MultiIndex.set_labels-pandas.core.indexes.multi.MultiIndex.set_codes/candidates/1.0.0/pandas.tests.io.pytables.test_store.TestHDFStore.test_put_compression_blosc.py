@td.skip_if_windows_python_3
def test_put_compression_blosc(self, setup_path):
    df = tm.makeTimeDataFrame()
    with ensure_clean_store(setup_path) as store:
        with pytest.raises(ValueError):
            store.put('b', df, format='fixed', complib='blosc')
        store.put('c', df, format='table', complib='blosc')
        tm.assert_frame_equal(store['c'], df)